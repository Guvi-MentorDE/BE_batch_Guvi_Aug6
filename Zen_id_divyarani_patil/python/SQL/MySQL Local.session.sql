CREATE TABLE test_table(
    fname VARCHAR(30)
);

insert INTO test_table(fname) values("divya");

SELECT * FROM test_table;

drop TABLE test_table;

use mydb2;

SELECT * FROM table_incr;

use mydb;

CREATE TABLE incr(
    id int auto_increment,
    fname VARCHAR(50),
    primary key (id)
);

SELECT * FROM incr;

INSERT into incr(fname) VALUES('jack');
INSERT into incr(fname) VALUES('Adam');
INSERT into incr(fname) VALUES('pia');
INSERT into incr(fname) VALUES('elle');

select * FROM incr ORDER BY fname;

SELECT * FROM employees;

# list all employees who are getting salary more than 20000

select * FROM employees where salary > 30000;

# list all employees who are getting salary more than or equal to 20000

select * FROM employees where salary >= 30000;

# list all employees who are getting less than 20000

select * FROM employees where salary <=30000;

ALTER TABLE employees add column age int;

SELECT * FROM employees;

INSERT INTO employees(age) values(20);
INSERT INTO employees(age) values(50);
INSERT INTO employees(age) values(30);
INSERT INTO employees(age) values(60);
INSERT INTO employees(age) values(25);

alter TABLE employees drop column age;

SELECT * FROM employees WHERE hiring_date = '2021-09-13' and salary <50000;

# get all those employees whose name starts with 'S'

SELECT * FROM employees where name like 'S%';

#get all the employees whose name starts with 'sm'

select * FROM employees where name like 'sm%';

# get all those employees whose name ends with 'l'

select * from employees where name like '%h';

# get all those employees whose name starts with 'S' and ends with 'k'

select * from employees where name like 's%h';

# Get all those employees whose name will have exact 5 characters

select * from employees where name like '______';

# Return all those employees whose name contains atleast 5 characters

select * from employees where name like '%_____%';

