--solution for q6 - some gaps need to revisit the logic
with cte1 as 
(
	select distinct id ,login_date from logins 
)
, cte2 as (
	select *
		,date_sub(login_date, interval row_number() over (partition by id order by login_date) day) as bucket
	from cte1
)
, cte3 as (
	select *
	,count(*) over(partition by id, bucket) as cnt
	from cte2
)
select distinct c.id, a.name 
from cte3 c
inner join accounts a
on c.id = a.id
where c.cnt >=5 ;



--create table scripts and data loading scripts
create table accounts
(
	id int
    ,name varchar(100)
);

create table logins
(
	id int
    ,login_date date
);

insert into accounts values
 (1,'Winston')
,(7,'Jonathan');

insert into logins values 
 (7  ,'2020-05-30')
,(1  ,'2020-05-30')
,(7  ,'2020-05-31')
,(7  ,'2020-06-01')
,(7  ,'2020-06-02')
,(7  ,'2020-06-02')
,(7  ,'2020-06-03')
,(1  ,'2020-06-07')
,(7  ,'2020-06-10');