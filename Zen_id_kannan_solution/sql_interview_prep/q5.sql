--solution for q5
select 
	 p.product_name
    ,sum(o.unit) as units
from products p
inner join orders o
	on p.product_id = o.product_id
where month(order_date)=2 and year(order_date)=2020
	group by p.product_name
	having sum(o.unit) >= 100;


--create table and data insert scripts
create table products
(
	 product_id int
	,product_name	varchar(50)
    ,product_category varchar(20)
);

create table orders
(
	 product_id int
    ,order_date date
    ,unit		int
);

insert into products values
 (1           ,'Science Solutions'		,'Book')
,(2           ,'Jewels of Stringology'	,'Book')
,(3           ,'HP'						,'Laptop')
,(4           ,'Lenovo'					,'Laptop')
,(5           ,'Science Kit'			,'T-shirt');

insert into orders values
 (1           ,'2020-02-05', 60 )
,(1           ,'2020-02-10', 70 )
,(2           ,'2020-01-18', 30 )
,(2           ,'2020-02-11', 80 )
,(3           ,'2020-02-17', 2  )
,(3           ,'2020-02-24', 3  )
,(4           ,'2020-03-01', 20 )
,(4           ,'2020-03-04', 30 )
,(4           ,'2020-03-04', 60 )
,(5           ,'2020-02-25', 50 )
,(5           ,'2020-02-27', 50 )
,(5           ,'2020-03-01', 50 );