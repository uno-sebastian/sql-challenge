-- Drop table if exists
DROP TABLE IF EXISTS titles;

-- Create new table to import data
CREATE TABLE titles (
	title_id VARCHAR,
	title VARCHAR
);

-- Import the data
INSERT INTO titles (title_id, title)
VALUES
	('s0001', 'Staff'),
	('s0002', 'Senior Staff'),
	('e0001', 'Assistant Engineer'),
	('e0002', 'Engineer'),
	('e0003', 'Senior Engineer'),
	('e0004', 'Technique Leader'),
	('m0001', 'Manager');

SELECT * FROM titles;