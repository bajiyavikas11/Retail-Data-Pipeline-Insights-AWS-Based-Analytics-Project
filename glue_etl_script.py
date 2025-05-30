import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load datasets
customers = glueContext.create_dynamic_frame.from_catalog(database="retail", table_name="customers_csv")
orders = glueContext.create_dynamic_frame.from_catalog(database="retail", table_name="orders_csv")
products = glueContext.create_dynamic_frame.from_catalog(database="retail", table_name="products_csv")

# Join and transform
joined = Join.apply(orders, customers, 'customer_id', 'customer_id')
joined = Join.apply(joined, products, 'product_id', 'product_id')
cleaned = DropFields.apply(joined, ['unnecessary_column'])

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame = cleaned,
    connection_type = "s3",
    connection_options = {"path": "s3://retail-output-bucket/cleaned/"},
    format = "parquet"
)

job.commit()
