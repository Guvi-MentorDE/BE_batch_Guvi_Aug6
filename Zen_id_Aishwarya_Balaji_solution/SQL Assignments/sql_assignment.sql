-----Data set:
--------------
create database mydb;
use mydb;
show tables;

create table orders
(
 cust_id int,
 order_id int,
 country varchar(50),
 state varchar(50),
 order_amt int(100)
);


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


create table sales
(
 cust_id int,
 sale_date int,
 delivery_status varchar(100),
);
-----------------------Solution / Fix ----------------------
create table sales
(
 cust_id int,
 sale_date int,
 delivery_status varchar(100)
);
ALTER TABLE sales MODIFY COLUMN sale_date DATE

---------------------------------------------------
insert into orders sales(1,'2023-05-01','pending');
insert into orders sales(1,'2023-05-02','inprogress');

insert into orders sales(3,'2023-05-01','pending');
insert into orders sales(3,'2023-05-02','inprogress');
insert into orders sales(3,'2023-05-03','completed');

insert into orders sales(7,'2023-05-01','completed');
insert into orders sales(7,'2023-05-01','inprogress');
insert into orders sales(7,'2023-04-31','pending');

insert into orders sales(6,'2023-05-01','completed');
insert into orders sales(6,'2023-04-31','pending');

insert into orders sales(5,'2023-04-31','pending');

-----------------------------Solution / Fix------------------------------------------
insert into sales values(1,'2023-05-01','pending');
insert into sales values(1,'2023-05-02','inprogress');

insert into sales values(3,'2023-05-01','pending');
insert into sales values(3,'2023-05-02','inprogress');
insert into sales values(3,'2023-05-03','completed');

insert into sales values(7,'2023-05-01','completed');
insert into sales values(7,'2023-05-01','inprogress');
insert into sales values(7,'2023-04-31','pending');

insert into sales values(6,'2023-05-01','completed');
insert into sales values(6,'2023-04-31','pending');

insert into sales values(5,'2023-04-31','pending');


--------Q1) find the country which has 3 most highest no of orders ?  //solve:

-------result : country , orders 

-------Solution 1:
SELECT country, COUNT(*) AS orders 
FROM orders 
GROUP BY country 
HAVING COUNT(*)>0 
LIMIT 3;

-------Solution 2:
SELECT country, COUNT(order_id) AS orders 
FROM orders 
GROUP BY country 
HAVING COUNT(order_id)>0 
LIMIT 3;

-------Solution 3:
SELECT country, COUNT(order_id) AS orders 
FROM orders 
GROUP BY country 
ORDER BY COUNT(order_id) desc 
LIMIT 3;

-------Solution 4:
SELECT tmp.country, MAX(orders) AS orders FROM (
    SELECT country, row_number() OVER(PARTITION BY country ORDER BY COUNT(order_id) desc) AS orders 
    FROM orders
) tmp 
GROUP BY tmp.country 
ORDER BY MAX(orders) desc
LIMIT 3;

-------Solution 5:
SELECT tmp.country, MAX(orders) AS orders FROM (
    SELECT country, COUNT(state) OVER(PARTITION BY country ORDER BY order_amt desc) AS orders 
    FROM orders
) tmp 
GROUP BY tmp.country 
ORDER BY MAX(orders) desc
LIMIT 3;

----------Q2) sum of order amounts for each country. 

----------result ; country , sum of order amounts. 

-------Solution 1:
SELECT country, SUM(order_amt) AS sum_of_order_amounts 
FROM orders 
GROUP BY country;


----------Q3) provide ranking for the countries based on the total amount of order. 
----------result : rank, country, total amount  of orders. 

-------Solution 1:
SELECT RANK() OVER(ORDER BY tmp.country) AS 'rank', tmp.country, MAX(tmp.order_amt) AS  total_amt_of_orders
FROM (
    SELECT country, SUM(order_amt) OVER(PARTITION BY country ORDER BY order_id desc) AS order_amt 
    FROM orders
    ) tmp 
GROUP BY country;


----------Q4) join sales vs orders. 
----------find the orders that are still pedning to be delivered 

----------result : only cust_id , pending status 



----------Q5) compare sales from todays date with previous date. 

----------all the sales happened on '2023-05-01' vs '2023-04-31'

----------result : current row , previous date , diff. 