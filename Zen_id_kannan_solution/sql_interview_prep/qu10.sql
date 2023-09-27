--solution for q10
with cte as 
(
	select 
		*, 
        row_number() over(partition by username order by startdate desc) as rn
	from useractivity
)
select 
	 username
    ,activity
    ,startdate
    ,enddate
from cte where rn = 1;

--create table and data insert scripts
create table useractivity
(
	 username varchar(100)
    ,activity varchar(50)
    ,startdate date
    ,enddate date
);

insert into useractivity values
 ('Alice','Travel' ,'2020-02-12','2020-02-20')
,('Alice','Dancing','2020-02-21','2020-02-23')
,('Alice','Travel' ,'2020-02-24','2020-02-28')
,('Bob'  ,'Travel' ,'2020-02-11','2020-02-18');