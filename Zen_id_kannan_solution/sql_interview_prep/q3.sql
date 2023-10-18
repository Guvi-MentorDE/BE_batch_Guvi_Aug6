--solution q3
select 
	distinct c.title
from tvprogram p
	join content c on p.content_id = c.content_id
where 
	c.kids_content = 'Y'
	and month(p.program_date)=6 
    and year(p.program_date)=2020;

--create table script    
create table tvprogram
(
	 program_date datetime
	,content_id int
    ,channel varchar(50)
);

create table content
(
	 content_id 	int
    ,title			varchar(100)
    ,kids_content	char(1)
    ,content_type	varchar(20)
);

--data load scripts
insert into tvprogram values
 ('2020-06-10 08:00',    1            ,'LC-Channel')
,('2020-05-11 12:00',    2            ,'LC-Channel')
,('2020-05-12 12:00',    3            ,'LC-Channel')
,('2020-05-13 14:00',    4            ,'Disney Ch')
,('2020-06-18 14:00',    4            ,'Disney Ch')
,('2020-07-15 16:00',    5            ,'Disney Ch');

insert into content values
 (1          ,'ScienceFiction Movie','N','Movies')
,(2          ,'Alg. for Kids'		,'Y','Series')
,(3          ,'Database Sols'		,'N','Series')
,(4          ,'Aladdin'				,'Y','Movies')
,(5          ,'Cinderella'			,'Y','Movies');