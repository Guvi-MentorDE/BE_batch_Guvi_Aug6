--------------------
show databases;

create database mydb;

use mydb;
--------------------

create table if not exists orders (cust_id integer, order_id integer, country varchar(50), state varchar(50), order_amt integer(100));

show tables;

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
------------------------
#Q1) find the country which has 3 most highest no of orders ?  //solve:
#result : country , orders

SELECT country, order_amt as orders FROM orders order by order_amt desc limit 3; #1

#Q2) sum of order amounts for each country.
#result ; country , sum of order amounts.

select country, sum(order_amt) as orders from orders group by country order by sum(order_amt) desc; #2

#Q3) provide ranking for the countries based on the total amount of order. 
#result : rank, country, total amount  of orders.

select rank() over(order by order_amt desc) as ranks, country, order_amt as total_amt_orders from orders; #3

------------------------

create table if not exists sales(cust_id int, sale_date date, delivery_status varchar(100));

insert into sales values(1,'2023-05-01','pending');
insert into sales values(1,'2023-05-02','inprogress');

insert into sales values(3,'2023-05-01','pending');
insert into sales values(3,'2023-05-02','inprogress');
insert into sales values(3,'2023-05-03','completed');

insert into sales values(7,'2023-05-01','completed');
insert into sales values(7,'2023-05-01','inprogress');
insert into sales values(7,'2023-04-30','pending');

insert into sales values(6,'2023-05-01','completed');
insert into sales values(6,'2023-04-30','pending');

insert into sales values(5,'2023-04-30','pending');

select * from sales;
---------------------------
#Q4) join sales vs orders.
#find the orders that are still pending to be delivered
#result : only cust_id , pending status

select s.cust_id, s.delivery_status as pending_status
from orders o
right join sales s on o.cust_id = s.cust_id where s.delivery_status = "pending"; #4

#Q5) compare sales from todays date with previous date. 
#all the sales happened on '2023-05-01' vs '2023-04-31'
#result : current row , previous date , diff.

#I can't get correct solution for 5th question
select o.cust_id, s.sale_date as previous_date, lead(o.order_amt, 1) over(order by s.sale_date desc) as diff
from sales s
right join orders o on s.cust_id = o.cust_id;