/*  Assignments  -  SQL
    Author       -  Devendra Kumar Rajendran  */
    
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

desc orders ;

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

Select * from orders ;

create table sales
(
 cust_id int,
 sale_date DATE ,
 delivery_status varchar(100)
);

desc sales; 

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

/* as received an error for April month,  that has only 30 days, updated the date value as "2023-4-30" in the table */

Select * from sales ;


/*Q1 : find the country which has 3rd most highest no of orders ?  //solve:  
result : country , orders                                                 */

/* Solution  - 3rd Most highest number of orders */  

SELECT tmp2.* FROM(
SELECT RANK() OVER(ORDER BY tmp.no_of_orders desc ) AS most_highest_no_orders, country, tmp.no_of_orders FROM 
(SELECT country, count(order_id) AS no_of_orders 
FROM orders 
GROUP BY country) tmp)tmp2
WHERE tmp2.most_highest_no_orders = 3;

/* Q2  - sum of order amounts for each country. 
result ; country , sum of order amounts.      */

/* Solution */

SELECT country, SUM(order_amt) AS sum_of_order_amt 
FROM orders 
GROUP BY country ;


/* Q3  - provide ranking for the countries based on the total amount of order. 
result : rank, country, total amount  of orders.                                 */
/* Solution - 1 */

SELECT RANK() OVER(order by tmp.total_amt_of_orders DESC) AS rank_number, tmp.country, tmp.total_amt_of_orders 
FROM (SELECT * , SUM(order_amt) OVER(PARTITION BY country) AS total_amt_of_orders 
    FROM orders) tmp 
    group by country, total_amt_of_orders ;
    

/* Solution - 2 */

SELECT 
RANK() OVER(ORDER BY SUM(order_amt) DESC ) AS rank_number , country, sum(order_amt) AS total_amt_of_orders
FROM orders
GROUP BY country ;

/* Q4  -  join sales vs orders. find the orders that are still pedning to be delivered
result -> order_id , cust_id, pending status                                            */

/* Solution  - 1 */

SELECT o.order_id , o.cust_id, s.delivery_status 
FROM orders o 
JOIN sales s 
ON s.cust_id = o.cust_id 
WHERE delivery_status IN ('pending') 
ORDER BY o.order_id;

/* Solution  - 2 */

SELECT o.order_id , o.cust_id, s.delivery_status 
FROM orders o 
JOIN sales s 
ON s.cust_id = o.cust_id 
WHERE delivery_status = 'pending' 
ORDER BY o.order_id;


/* Q5  -  Q5) compare sales from todays date with previous date. 
result : current row , previous date , diff.  */

/* Solution  */

SELECT 
tmp.sale_date as "Current_date", 
SUM(order_amt) as Current_date_total_sale_amount,
LAG (SUM(order_amt),1,0)  OVER(ORDER BY tmp.sale_date) AS prev_date_total_sale_amount,
SUM(order_amt) - LAG (SUM(order_amt),1,0)  OVER(ORDER BY tmp.sale_date) AS diff_total_sale_amount 
FROM(
SELECT order_id, country, order_amt, sale_date
 FROM orders o
 JOIN sales s
 ON o.cust_id= s.cust_id
  ) tmp  
  GROUP BY sale_date
  ORDER BY sale_date;
  
  

