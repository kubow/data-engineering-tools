
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

WITH customer_revenue AS (
    SELECT
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        SUM(s.total_amount) AS total_revenue
    FROM
        {{ source('business_data', 'purchase_history_dataset') }} s
    JOIN
        {{ source('business_data', 'customer_profile_dataset') }} c
    ON
        s.customer_id = c.customer_id
    GROUP BY
        c.customer_id, c.first_name, c.last_name
)
SELECT
    customer_id,
    customer_name,
    total_revenue
FROM
    customer_revenue
ORDER BY
    total_revenue DESC
LIMIT 100
