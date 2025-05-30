-- Total sales per category
SELECT 
    p.category,
    SUM(o.quantity * p.price) AS total_sales
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

-- Top 10 selling products
SELECT 
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 10;
