-- Drop table if exists
DROP TABLE IF EXISTS departments;

-- Create new table to import data
CREATE TABLE departments (
	dept_no VARCHAR,
	dept_name VARCHAR
);

-- Import the data
INSERT INTO departments (dept_no, dept_name)
VALUES
	('d001', 'Marketing'),
	('d002', 'Finance'),
	('d003', 'Human Resources'),
	('d004', 'Production'),
	('d005', 'Development'),
	('d006', 'Quality Management'),
	('d007', 'Sales'),
	('d008', 'Research'),
	('d009', 'Customer Service');

SELECT * FROM departments;