Data set:
--------------
create database mydb;
use mydb;
show tables;
------------------------------------------------------------
create table orders
(
 cust_id int,
 order_id int,
 country varchar(50),
 state varchar(50),
 order_amt int(100),
 primary key(order_id)
);
------------------------------------------------------------

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
-------------------------------------------------------------

create table sales
(
 cust_id int,
 sale_date int,
 delivery_status varchar(100)
);
------------------------------------------------------------------
--Alter Table column data type
alter table sales modify column sale_date date;
-------------------------------------------------------------------
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
--------------------------------------------------------------------

Q1) find the country which has 3 most highest no of orders ?  //solve:
        select country, count(*) as orders from orders group by country having count(*)>0 order by orders desc limit 3;
result : country , orders 

-------------------------------------------------------------------------------------------------------------------------------------------------
Q2) sum of order amounts for each country. 

 select country,sum(order_amt) as Total_amt from orders group by country;
+---------+-----------+
| country | Total_amt |
+---------+-----------+
| USA     |     66400 |
| INDIA   |     61300 |
| UK      |     13000 |
+---------+-----------+
3 rows in set (0.00 sec)
result ; country , sum of order amounts. 

-------------------------------------------------------------------------------------------------------------------------------------------------
Q3) provide ranking for the countries based on the total amount of order. 

select rank() over (order by sum(order_amt) desc) as Country_Rank,
    -> country, sum(order_amt) as Total_sum_of_orders
    -> from orders group by country
    -> order by sum(order_amt) desc;
+--------------+---------+---------------------+
| Country_Rank | country | Total_sum_of_orders |
+--------------+---------+---------------------+
|            1 | USA     |               66400 |
|            2 | INDIA   |               61300 |
|            3 | UK      |               13000 |
+--------------+---------+---------------------+
3 rows in set (0.00 sec)

result : rank, country, total amount  of orders. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q4) join sales vs orders. 
find the orders that are still pedning to be delivered 


   select o.order_id,o.cust_id,s.sale_date,s.delivery_status from orders o join sales s on o.cust_id=s.cust_id where s.delivery_status="pending";
+----------+---------+------------+-----------------+
| order_id | cust_id | sale_date  | delivery_status |
+----------+---------+------------+-----------------+
|      100 |       1 | 2023-05-01 | pending         |
|      109 |       5 | 2023-04-30 | pending         |
|      120 |       3 | 2023-05-01 | pending         |
|      131 |       1 | 2023-05-01 | pending         |
|      142 |       6 | 2023-04-30 | pending         |
|      150 |       7 | 2023-04-30 | pending         |
+----------+---------+------------+-----------------+
6 rows in set (0.01 sec)

result -> order_id , cust_id, pending status 

--------------------------------------------------------------------------------------------------------------------------------------------------------
Q5) compare sales from todays date with previous date. 

all the sales happened on '2023-05-01' vs '2023-04-30'


 select * from(select s.sale_date as current_dated,
    -> sum(o.order_amt) from sales s inner join orders o on s.cust_id = o.cust_id
    -> group by s.sale_date
    -> order by s.sale_date) as temp;
+---------------+------------------+
| current_dated | sum(o.order_amt) |
+---------------+------------------+
| 2023-04-30    |            29500 |
| 2023-05-01    |            44300 |
| 2023-05-02    |            18900 |
| 2023-05-03    |             2000 |
+---------------+------------------+
4 rows in set (0.00 sec)


select temp.current_dated as current_dated,
    -> lag(temp.current_dated,1) over (order by temp.current_dated) as previous_date,
    -> (lag(temp.total_sales,1) over (order by temp.current_dated) - temp.total_sales) as diff
    -> from
    -> (select s.sale_date as current_dated,
    -> sum(o.order_amt) as total_sales
    -> from sales as s
    -> inner join orders as o
    -> on s.cust_id=o.cust_id
    -> group by s.sale_date
    -> order by s.sale_date) as temp;
+---------------+---------------+--------+
| current_dated | previous_date | diff   |
+---------------+---------------+--------+
| 2023-04-30    | NULL          |   NULL |
| 2023-05-01    | 2023-04-30    | -14800 |
| 2023-05-02    | 2023-05-01    |  25400 |
| 2023-05-03    | 2023-05-02    |  16900 |
+---------------+---------------+--------+
4 rows in set (0.01 sec)


result : current row , previous date , diff. 
----------------------------------------------------------------------------------------------------------------------------------------------------