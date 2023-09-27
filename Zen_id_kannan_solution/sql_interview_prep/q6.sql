--solution for q6 - some gaps need to revisit the logic
with cte as 
(
	select 
		 l.id
		,l.login_date
        ,count(*) over(partition by l.id order by l.login_date range between interval '5' day preceding and current row) cnt
		,datediff(lead(l.login_date) over(partition by l.id order by l.login_date), l.login_date) as diff
	from (
		select distinct id, login_date from logins
	) l
)
select distinct 
     c.id
    ,a.name 
from cte c
join accounts a
    on c.id = a.id
where c.cnt = 5;


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