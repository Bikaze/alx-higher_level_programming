-- This script displays the top 3 of the cities temperature during july and August ordered by temperature(descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp desc
LIMIT 3;
