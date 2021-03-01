# Sebastian's SQL Challenge - Employee Database: A Mystery in Two Parts

![sql.png](sql.png)

## Background

It is a beautiful spring day, and it is two weeks since you have been hired as a new data engineer at Pewlett Hackard. Your first major task is a research project on employees of the corporation from the 1980s and 1990s. All that remain of the database of employees from that period are six CSV files.

## Instructions

#### Data Engineering

* Use the information you have to create a table schema for each of the six CSV files.

  * For the primary keys check to see if the column is unique, otherwise create a [composite key](https://en.wikipedia.org/wiki/Compound_key). Which takes two primary keys in order to uniquely identify a row.
  * Be sure to create tables in the correct order to handle foreign keys.

* Import each CSV file into the corresponding SQL table.

#### Data Analysis

Once you have a complete database, do the following:

[1. List the following details of each employee: employee number, last name, first name, sex, and salary.](EmployeeSQL/Q1_EmployeeDetails.sql)

[2. List first name, last name, and hire date for employees who were hired in 1986.](EmployeeSQL/Q2_1986Hires.sql)

[3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.](EmployeeSQL/Q3_DepartmentManagers.sql)

[4. List the department of each employee with the following information: employee number, last name, first name, and department name.](EmployeeSQL/Q4_EmployeeAndDepartment.sql)

[5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."](EmployeeSQL/Q5_EmployeesHerculesB.sql)

[6. List all employees in the Sales department, including their employee number, last name, first name, and department name.](EmployeeSQL/Q6_SalesEmployeeAndDepartment.sql)

[7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.](EmployeeSQL/Q7_SalesAndDevelopmentEmployeeAndDepartment.sql)

[8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.](EmployeeSQL/Q8_LastNameFrequency.sql)

## Bonus

As you examine the data, you are overcome with a creeping suspicion that the dataset is fake. You surmise that your boss handed you spurious data in order to test the data engineering skills of a new employee. To confirm your hunch, you decide to take the following steps to generate a visualization of the data, with which you will confront your boss:

1. Create a histogram to visualize the most common salary ranges for employees.
![salary_ranges_for_employees.png](salary_ranges_for_employees.png)

2. Create a bar chart of average salary by title.
![average_salary_by_title.png](average_salary_by_title.png)

## Epilogue

Evidence in hand, you march into your boss's office and present the visualization. With a sly grin, your boss thanks you for your work. On your way out of the office, you hear the words, "Search your ID number." You look down at your badge to see that your employee ID number is 499942.
