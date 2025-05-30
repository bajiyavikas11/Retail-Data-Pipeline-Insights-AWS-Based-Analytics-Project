# 🛒 Retail Data Pipeline & Insights

A cloud-native retail analytics pipeline built using AWS services like S3, Glue, Athena, and QuickSight to automate ETL, querying, and dashboarding.

## 📦 Tech Stack
- **Languages:** Python, SQL
- **Services:** AWS S3, Glue, Athena, QuickSight
- **Tools:** PySpark, Glue Crawlers, Faker (for data generation)

## 📁 Dataset Summary
| File        | Rows | Description                        |
|-------------|------|------------------------------------|
| customers.csv | 1,000 | Customer demographics             |
| orders.csv    | 5,000 | Transactional order data          |
| products.csv  | 500   | Product catalog with categories   |

## 🔧 Architecture Overview
1. Data uploaded to S3
2. AWS Glue ETL jobs perform joins/cleansing
3. Transformed data stored back in S3
4. Glue Crawler creates schema in Glue Catalog
5. Athena runs SQL queries on structured data
6. QuickSight visualizes KPIs via dashboards

## 📊 Key Features
- ETL pipeline for customer, order, and product data
- Real-time KPIs by category and product
- QuickSight dashboards with filter support
- Audit and validation steps for data quality

## 🔮 Future Scope
- Real-time ingestion via AWS Kinesis
- NLP integration using SageMaker
- Cost-tracking across AWS services

---

📂 Directory

