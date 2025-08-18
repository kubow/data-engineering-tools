
-- Use the `ref` function to select from other models

WITH product_orders AS (
    SELECT
        p.product_id,
        p.product_name,
        COUNT(s.purchase_id) AS total_orders
    FROM 
        {{ source('business_data', 'purchase_history') }} s
    JOIN 
        {{ source('business_data', 'product') }} p
    ON 
        s.product_id = p.product_id
    GROUP BY 
        p.product_id, p.product_name
)
SELECT 
    product_id,
    product_name,
    total_orders
FROM 
    product_orders
ORDER BY 
    total_orders DESC
LIMIT 10