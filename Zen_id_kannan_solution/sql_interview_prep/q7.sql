--solution for q7
with cte as (
	select *, max(salary) over(partition by company_id) as max_salary
	from salaries
)
select 
	 company_id
    ,employee_id
    ,employee_name
    ,round(case 	when max_salary <1000 then salary
			when max_salary >= 1000 and max_salary <=10000 then salary - salary*0.24
            when max_salary > 10000 then salary - salary*0.49
		end) as salary
from cte;

--create table and data load scripts
create table salaries
(
	 company_id     int    
	,employee_id    int    
	,employee_name  varchar(50)
	,salary         int    
);

insert into salaries values
 ( 1          , 1           ,'Tony', 2000  )
,( 1          , 2           ,'Pronub', 21300 )
,( 1          , 3           ,'Tyrrox', 10800 )
,( 2          , 1           ,'Pam', 300   )
,( 2          , 7           ,'Bassem', 450   )
,( 2          , 9           ,'Hermione', 700   )
,( 3          , 7           ,'Bocaben', 100   )
,( 3          , 2           ,'Ognjen', 2200  )
,( 3          , 13          ,'Nyancat', 3300  )
,( 3          , 15          ,'Morninngcat', 1866  );
