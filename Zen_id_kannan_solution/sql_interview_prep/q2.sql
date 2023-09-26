--solution q2
select 
	 employee_id
	,count(employee_id) over(partition by team_id) as team_size
from employee
order by employee_id;

--create table script
create table employee (employee_id int, team_id int);

--data loading
insert into employee values
 (1       ,     8)
,(2       ,     8)
,(3       ,     8)
,(4       ,     7)
,(5       ,     9)
,(6       ,     9);