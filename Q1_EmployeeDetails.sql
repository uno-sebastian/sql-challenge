-- List the following details of each employee: 
-- employee number, last name, first name, sex, 
-- and salary.

SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM employees as e
JOIN salaries AS s 
ON (e.emp_no = s.emp_no);