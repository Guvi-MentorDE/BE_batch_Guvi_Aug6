/**
Author 			:	Kannan Kandasamy
Date			:	2023/sep/02
Details			:	SQL Assignment question 4,5
**/

use testdb;
use testsch;

#loading data
drop table sales;
#it has to be order_id instead of cust_id so that we will get cust_id by joining order_id and display only cust_id
create table sales
(
	 cust_id 			int 			
	,sale_date			date
	,delivery_status 	varchar(100)
);

#truncate table sales;

insert into sales VALUES(1,'2023-05-01','pending');
insert into sales VALUES(1,'2023-05-02','inprogress');

insert into sales VALUES(3,'2023-05-01','pending');
insert into sales VALUES(3,'2023-05-02','inprogress');
insert into sales VALUES(3,'2023-05-03','completed');

insert into sales VALUES(7,'2023-05-01','completed');
insert into sales VALUES(7,'2023-05-01','inprogress');
insert into sales VALUES(7,'2023-04-30','pending');

insert into sales VALUES(6,'2023-05-01','completed');
insert into sales VALUES(6,'2023-04-30','pending');

insert into sales VALUES(5,'2023-04-30','pending');

#Q4) join sales vs orders. 
#find the orders that are still pedning to be delivered 

#This query works for original table where sales having cust_id
select distinct
	 s.cust_id
    ,s.delivery_status
from sales s
join orders o
	on s.cust_id = o.cust_id
where s.delivery_status = 'pending'
order by s.cust_id;

#for this query we really dont need to join orders to get the deliver
#this will also give the same results as above
select distinct
	 s.cust_id
    ,s.delivery_status
from sales s
where s.delivery_status = 'pending'
order by s.cust_id;



#so i am creating sales_orders table which has only the order_id as below:
create table sales_orders
(
	 order_id 			int 			
	,sale_date			date
	,delivery_status 	varchar(100)
);

insert into sales_orders VALUES(100,'2023-05-01','pending');
insert into sales_orders VALUES(101,'2023-05-02','inprogress');

insert into sales_orders VALUES(103,'2023-05-01','pending');
insert into sales_orders VALUES(103,'2023-05-02','inprogress');
insert into sales_orders VALUES(103,'2023-05-03','completed');

insert into sales_orders VALUES(121,'2023-05-01','completed');
insert into sales_orders VALUES(121,'2023-05-01','inprogress');
insert into sales_orders VALUES(121,'2023-04-30','pending');

insert into sales_orders VALUES(142,'2023-05-01','completed');
insert into sales_orders VALUES(142,'2023-04-30','pending');

insert into sales_orders VALUES(142,'2023-04-30','pending');

select * from sales_orders;

#This gives by joining sales and orders tables and get attributes from different tables
select distinct
	 o.cust_id
    ,s.delivery_status
from orders o
join sales_orders s
	on s.order_id = o.order_id
where s.delivery_status = 'pending'
order by o.cust_id;




#Q5) compare sales from todays date with previous date. 

select 
	 s.cust_id
    ,o.order_amt as current_order_amount
    ,lag(o.order_amt,1,0) over(partition by s.cust_id order by s.sale_date) as prev_amount
	,(o.order_amt - lag(o.order_amt,1,0) over(partition by s.cust_id order by s.sale_date)) as Diff_amount
from sales s
join orders o
on s.cust_id = o.cust_id;

