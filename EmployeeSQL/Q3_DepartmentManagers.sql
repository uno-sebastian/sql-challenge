-- List the manager of each department with 
-- the following information: department number, 
-- department name, the manager's employee number, 
-- last name, first name.

SELECT i.dept_no, d.dept_name, i.emp_no, e.last_name, e.first_name
FROM dept_manager as i
	JOIN departments as d
	ON (i.dept_no = d.dept_no)
		JOIN employees as e
		ON (i.emp_no = e.emp_no);
