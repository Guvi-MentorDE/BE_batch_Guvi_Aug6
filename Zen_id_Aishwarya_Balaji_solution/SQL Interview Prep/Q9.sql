-- A university uses 2 data tables, student and department, to store data about its students
-- and the departments associated with each major.

-- Write a query to print the respective department name and number of students majoring in each
-- department for all departments in the department table (even ones with no current students).

-- Sort your results by descending number of students; if two or more departments have the same number of students, 
-- then sort those departments alphabetically by department name.

-- The student is described as follow:

-- | Column Name  | Type      |
-- |--------------|-----------|
-- | student_id   | Integer   |
-- | student_name | String    |
-- | gender       | Character |
-- | dept_id      | Integer   |
-- where student_id is the student's ID number, student_name is the student's name, gender is their gender, and dept_id is the department ID associated with their declared major.

-- And the department table is described as below:

-- | Column Name | Type    |
-- |-------------|---------|
-- | dept_id     | Integer |
-- | dept_name   | String  |
-- where dept_id is the department's ID number and dept_name is the department name.

--Here is an example input:
--student table:

--| student_id | student_name | gender | dept_id |
--|------------|--------------|--------|---------|
--| 1          | Jack         | M      | 1       |
--| 2          | Jane         | F      | 1       |
--| 3          | Mark         | M      | 2       |
--department table:

--| dept_id | dept_name   |
--|---------|-------------|
--| 1       | Engineering |
--| 2       | Science     |
--| 3       | Law         |
--The Output should be:

--| dept_name   | student_number |
--|-------------|----------------|
--| Engineering | 2              |
--| Science     | 1              |
--| Law         | 0              |

--Solution:

CREATE TABLE students(student_id INT, student_name VARCHAR(60), gender CHAR, dept_id INT);

CREATE TABLE departments(dept_id INT, dept_name VARCHAR(50));

INSERT INTO students VALUES(1, 'Jack', 'M', 1);
INSERT INTO students VALUES(2, 'Jane', 'F', 1);
INSERT INTO students VALUES(3, 'Mark', 'M', 2);

SELECT * FROM students;

INSERT INTO departments VALUES(1, 'Engineering');
INSERT INTO departments VALUES(2, 'Science');
INSERT INTO departments VALUES(3, 'Law');

SELECT * FROM departments;

SELECT DISTINCT dept_group.* 
FROM 
(
    SELECT dept_name, COUNT(stud.dept_id) OVER(PARTITION BY stud.dept_id) AS student_number 
    FROM departments dept 
    LEFT JOIN students stud on stud.dept_id = dept.dept_id
) dept_group  
ORDER BY dept_group.student_number desc;