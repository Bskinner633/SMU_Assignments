SELECT
	emp_no,
	last_name,
	first_name,
	gender
FROM
	employees 
WHERE 
	first_name = 'Hercules'
	AND last_name LIKE 'B%'
ORDER BY
	last_name ASC;