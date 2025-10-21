# Assignment

## Brief

Write the SQL statements for the following questions.

## Instructions

Paste the answer as SQL in the answer code section below each question.

### Question 1

Using the `claim` and `car` tables, write a SQL query to return a table containing `id, claim_date, travel_time, claim_amt` from `claim`, and `car_type, car_use` from `car`. Use an appropriate join based on the `car_id`.

Answer:

```sql
SELECT 
	cl.id, cl.claim_date, cl.travel_time, cl.claim_amt,
	c.car_type, c.car_use
FROM main.claim cl
INNER JOIN main.car c
ON cl.car_id = c.id
ORDER BY cl.claim_date DESC;
```

### Question 2

Write a SQL query to compute the running total of the `travel_time` column for each `car_id` in the `claim` table. The resulting table should contain `id, car_id, travel_time, running_total`.

Answer:

```sql
SELECT
	cl.id, cl.car_id, cl.claim_date, cl.travel_time, 
	SUM(travel_time) OVER (PARTITION BY car_id ORDER BY cl.claim_date) AS running_total
FROM main.claim cl
ORDER BY cl.car_id, cl.claim_date;
```

### Question 3

Using a Common Table Expression (CTE), write a SQL query to return a table containing `id, resale_value, car_use` from `car`, where the car resale value is less than the average resale value for the car use.

Answer:

```sql
ITH avg_value AS 
(
	SELECT 
		c.car_use, ROUND(AVG(resale_value),1) AS ave_value_by_use
	FROM main.car c
	GROUP by c.car_use
)
SELECT 
	c.id, c.car_use, c.resale_value, a.ave_value_by_use, 
	(a.ave_value_by_use - resale_value) AS value_diff
FROM main.car c
INNER JOIN avg_value a ON c.car_use = a.car_use
WHERE c.resale_value < a.ave_value_by_use
ORDER BY value_diff DESC;
```

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
