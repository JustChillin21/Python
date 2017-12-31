SELECT customers.first_name, customers.last_name, SUM(items.price) AS "Total Spent" from items
INNER JOIN purchases ON purchases.item_id = items.id
INNER JOIN customers ON purchases.customer_id=customers.id
GROUP BY customers.id
ORDER BY "Total Spent" DESC LIMIT 3;