
-- used beautify/reformat option to indent queries
-- corrected some data and syntax errors in the question 

create database mydb;
use mydb;
show tables;

CREATE TABLE orders (
    cust_id INT,
    order_id INT,
    country VARCHAR(50),
    state VARCHAR(50),
    order_amt INT
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

CREATE TABLE sales (
    cust_id INT,
    sale_date DATE,
    delivery_status VARCHAR(100)
);


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

-- Q1) find the country which has 3rd most highest no of orders ?  

SELECT 
    country
FROM
    orders
GROUP BY country
ORDER BY COUNT(country) DESC
LIMIT 3 OFFSET 2;

-- Q2) sum of order amounts for each country.

SELECT 
    country, SUM(order_amt)
FROM
    orders
GROUP BY country;

-- Q3) provide ranking for the countries based on the total amount of order. 
-- result : rank, country, total amount  of orders. 

SELECT 
    rank() over (order by sum(order_amt) desc ) as country_rank,
	country,
    sum(order_amt) as total_amountoforders
from 
	orders
group by
	country
order by 
    sum(order_amt) desc;
    
    
-- Q4) join sales vs orders. 
-- find the orders that are still pedning to be delivered 
-- result -> order_id , cust_id, pending status   

SELECT 
    o.order_id,
    o.cust_id,
    s.delivery_status AS pending_status
FROM
    orders AS o
        INNER JOIN
    sales AS s ON o.cust_id = s.cust_id
WHERE
    s.delivery_status = 'pending';
	
-- Q5) compare sales from todays date with previous date. 
-- all the sales happened on '2023-05-01' vs '2023-04-31'
-- result : current row , previous date , diff.  

-- sales data grouped under dates , just the results of subquery
SELECT 
    *
FROM
    (SELECT 
        s.sale_date AS current_datee,
            SUM(o.order_amt) AS total_sales
    FROM
        sales AS s
    INNER JOIN orders AS o ON s.cust_id = o.cust_id
    GROUP BY s.sale_date
    ORDER BY s.sale_date) AS temp ; 


-- applying queries to visualise difference 
SELECT 
    temp.current_datee as current_datee,
    lag(temp.current_datee,1) over (order by temp.current_datee) as previous_date,
    (lag(temp.total_sales,1) over ( order by temp.current_datee) - temp.total_sales) as diff
FROM
    (SELECT 
        s.sale_date AS current_datee,
        SUM(o.order_amt) AS total_sales
    FROM
        sales AS s
    INNER JOIN orders AS o ON s.cust_id = o.cust_id
    GROUP BY s.sale_date
    ORDER BY s.sale_date) AS temp;
