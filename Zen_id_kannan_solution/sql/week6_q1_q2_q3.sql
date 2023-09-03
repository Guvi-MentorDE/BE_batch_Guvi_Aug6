/**
Author 			:	Kannan Kandasamy
Date			:	2023/sep/02
Details			:	SQL Assignment question 1
**/

use testdb;
use testsch;
drop table orders;

#creating orders tables
create table orders
(
	 cust_id int,
	 order_id int,
	 country varchar(50),
	 state varchar(50),
	 order_amt int
);

#loading data into orders
insert into orders values(1,100,'USA','Seattle','10000');
insert into orders values(2,101,'INDIA','UP','12000');
insert into orders values(2,103,'INDIA','Bihar','42000');
insert into orders values(4,108,'USA','WDC','32000');
insert into orders values(5,109,'UK','London','13000');
insert into orders values(4,110,'USA','WDC','1000');
insert into orders values(3,120,'INDIA','AP','2000');
insert into orders values(2,121,'INDIA','Goa','5300');
insert into orders values(1,131,'USA','Seattle','6900');
insert into orders values(6,142,'USA','Seattle','7600');
insert into orders values(7,150,'USA','Seattle','8900');

select * from orders;

#Q1) find the country which has 3 most highest no of orders ?  //solve:
select 	
	 country
	,count(1) as orders 
from orders
group by country
having count(*) >= 3;

#Q2) sum of order amounts for each country. 
select 	
	 country
	,sum(order_amt) as sum_of_order_amounts 
from orders
group by country
order by country;

#Q3) provide ranking for the countries based on the total amount of order. 
select 
	 rank() over(order by a.total_order_amt desc) as Rank_of_Country
    ,a.country 				as	Country
    ,a.total_order_amt		as 	Total_amount_of_orders
from (
	select country, sum(order_amt) as total_order_amt 
		from orders
    group by country
    ) a;

