show tables;

drop TABLE orders;

CREATE TABLE IF NOT EXISTS orders(
    cust_id int,
    order_id int,
    country varchar(50),
    state varchar(50),
    order_amt int(100)
);

select * FROM orders;
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

CREATE TABLE IF NOT EXISTS sales(
    customer_id int,
    sale_date int,
    delivery_status varchar(100)
);

select * FROM sales;

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

alter TABLE sales modify column sale_date date;


--Q1: find the country which has 3 most highest no of orders?

select country,max(order_amt) as highest from orders GROUP BY country limit 3;

--Q2: sum of order amounts for each country 

select country , sum(order_amt) OVER(PARTITION BY country) as total from orders;

--Q3: provide ranking for the countries based on the total amount of order 

--SELECT rank() OVER(PARTITION BY country ORDER BY order_amt) as rank_val 
--from (SELECT country, sum(order_amt) from orders ) as total  group BY country;

--(merge two queries )

select country,rank() OVER(PARTITION BY country ORDER BY order_amt DESC)
as rank_val from orders; 

select sum(order_amt) as total_amt_orders , country
    from orders GROUP BY country;


--Q4: join sales vs orders cust_id , pending status 

SELECT o.cust_id , s.delivery_status from orders o
join sales s
on o.cust_id = s.customer_id
where delivery_status = 'pending';

--Q5: compare sales from today date with previous date 
-- all sales happened on '2023-05-01' vs '2023-04-30'

SELECT * , 
lag(sale_date,1) OVER(ORDER BY sale_date rows BETWEEN 1 PRECEDING AND CURRENT ROW) as prev_date
from sales;