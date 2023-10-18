--solution for q8
with cte as (
	select 
		*
		,lag(num) over(order by id) as lnum 
		,case when num = lag(num) over(order by id) then 0 		#to create same group 
			else 1 end as cnt
	from numbers
)
, cte2 as (
	select *, sum(cnt) over(order by id) as sm from cte  		#bucketing consecutive numbers
)
, cte3 as (
	select *, count(*) over(partition by sm) smcnt from cte2	
)
select distinct num as cunsecutiveNums 
	from cte3 
where smcnt >=3 ;

--create table and data load scripts
create table numbers 
(
	 id int
    ,num int
);

insert into numbers values
 ( 1  ,  1  )
,( 2  ,  1  )
,( 3  ,  1  )
,( 4  ,  2  )
,( 5  ,  1  )
,( 6  ,  2  )
,( 7  ,  2  );    