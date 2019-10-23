SELECT 
	last_name,
	COUNT (last_name) AS LastNameCount
FROM
	employees
group by
	last_name
ORDER BY
	LastNameCount DESC;