--solution for q4
with cte as (
	select 
		 player_id 
		,device_id
		,row_number() over(partition by player_id order by event_date) rn
	from activity
)
select 
	 player_id
    ,device_id 
from cte where rn = 1;

--create table and data load queries
create table activity
(
	 player_id int
	,device_id int
    ,event_date date
    ,games_played int
);

insert into activity values
 (1         , 2         ,'2016-03-01', 5 )
,(1         , 2         ,'2016-05-02', 6 )
,(2         , 3         ,'2017-06-25', 1 )
,(3         , 1         ,'2016-03-02', 0 )
,(3         , 4         ,'2018-07-03', 5 );