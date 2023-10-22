--solution for q9
select 
	 d.dept_name
    ,count(s.student_id) as student_number
from department d
left join student s on s.dept_id = d.dept_id
group by d.dept_name
order by student_number desc;

--create table and data load scripts
create table student
(
	 student_id int
    ,student_name varchar(100)
    ,gender	char(1)
    ,dept_id int
);

create table department
(
	 dept_id int
    ,dept_name varchar(100)
);

insert into student values
 ( 1    ,'Jack'         ,'M', 1 )
,( 2    ,'Jane'         ,'F', 1 )
,( 3    ,'Mark'         ,'M', 2 );

select * from student;
select * from department;

insert into department values 
 (1, 'Engineering')
,(2, 'Science')
,(3, 'Law');
