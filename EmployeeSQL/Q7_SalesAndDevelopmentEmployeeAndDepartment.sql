-- List all employees in the Sales and Development 
-- departments, including their employee number,
-- last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM dept_emp as i
	JOIN employees as e
	ON (i.emp_no = e.emp_no)
		JOIN departments as d
		ON (i.dept_no = d.dept_no)
			WHERE d.dept_name = 'Sales' OR d.dept_name = 'Development';