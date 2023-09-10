/*                                                   
                                                ASSIGNMENT-1


                                        Author   :   Mohammad Hammad Ahmad
                                        Subject  :   SQL
                                        Date     :   10/09/2023


*/

/*

DATA SET

*/
/*

 Creating a database called mydb

*/

CREATE DATABASE mydb;

/*

 Checking that our database 'mydb' is in the list of databases.

*/

SHOW DATABASES;

/*

Selecting our Created database 'mydb' to work in this database 

*/

USE mydb;

/*

 Checking how many tables are there in our created database 'mydb'

*/

SHOW TABLES;

/*

Creating a table named 'orders' in our created database 'mydb'

*/

CREATE TABLE orders (
 cust_id INTEGER,
 order_id INTEGER,
 country VARCHAR(50),
 state VARCHAR(50),
 order_amt INTEGER(100)
);

/*

Inserting values in our newly created table 'orders' in our created database 'mydb'

*/

INSERT INTO orders VALUES(1,100,'USA','Seattle','10000');
INSERT INTO orders VALUES(2,101,'INDIA','UP','12000');
INSERT INTO orders VALUES(2,103,'INDIA','Bihar','42000');
INSERT INTO orders VALUES(4,108,'USA','WDC','32000');
INSERT INTO orders VALUES(5,109,'UK','London','13000');
INSERT INTO orders VALUES(4,110,'USA','WDC','1000');
INSERT INTO orders VALUES(3,120,'INDIA','AP','2000');
INSERT INTO orders VALUES(2,121,'INDIA','Goa','5300');
INSERT INTO orders VALUES(1,131,'USA','Seattle','6900');
INSERT INTO orders VALUES(6,142,'USA','Seattle','7600');
INSERT INTO orders VALUES(7,150,'USA','Seattle','8900');

/*

Creating another table by the name 'sales' in our created database 'mydb'

*/

CREATE TABLE sales (
 cust_id INTEGER,
 sale_date DATE,
 delivery_status VARCHAR(100)
 );
 
 /*

Inserting values in our newly created table 'sales' in our created database 'mydb'

Changes in input data : The 1st, 2nd, and 4th records from the bottom had the incorrect date '2023-04-31' 
because April only has 30 days.
So i changed the date from '2023-04-31' to '2023-04-30' in the 1st, 2nd and 4th 
records from the bottom.

*/
 
INSERT INTO sales VALUES(1,'2023-05-01','pending');
INSERT INTO sales VALUES(1,'2023-05-02','inprogress');
INSERT INTO sales VALUES(3,'2023-05-01','pending');
INSERT INTO sales VALUES(3,'2023-05-02','inprogress');
INSERT INTO sales VALUES(3,'2023-05-03','completed');
INSERT INTO sales VALUES(7,'2023-05-01','completed');
INSERT INTO sales VALUES(7,'2023-05-01','inprogress');
INSERT INTO sales VALUES(7,'2023-04-30','pending');
INSERT INTO sales VALUES(6,'2023-05-01','completed');
INSERT INTO sales VALUES(6,'2023-04-30','pending');
INSERT INTO sales VALUES(5,'2023-04-30','pending');

/*

Solving the questions given below with the help of newly created tables 'orders' and 'sales' in our database 'mydb'

*/

/*

QUESTION 1: Find the country which has 3 most highest no of orders ? 

Format of result : country , orders 

*/

# SOLUTION 1:
 
SELECT country, COUNT(*) AS `orders`
FROM orders
GROUP BY country
HAVING COUNT(*)>=3;

/*

QUESTION 2: Find the sum of order amounts for each country. 

Format of result : country , sum of order amounts.

*/

# SOLUTION 2:

SELECT country, SUM(order_amt) AS `sum of order amounts`
FROM orders
GROUP BY country;


/*

QUESTION 3: Provide ranking for the countries based on the total amount of order. 

Format of result : rank, country, total amount  of orders. 

*/

# SOLUTION 3:

SELECT 
    RANK() OVER (ORDER BY SUM(order_amt) DESC) AS `rank`,
    country,
    SUM(order_amt) AS `total amount of orders`
FROM orders
GROUP BY country;

/*

QUESTION 4: Join sales vs orders. Find the orders that are still pending to be delivered 

Format of result : only cust_id , pending status 
BUT
My format of result : only cust_id , order_id, pending status 

( i have added field 'order_id' in the output because for cust_id 1 there are two entries as 'pending'
   in filed 'delivery_status of table 'sales'
   also these two entries are associated with two different order_id from table 'orders'
   which means the customer with cust_id 1 has placed 2 orders separately and 
   both are showing delivery_status as 'pending' )

*/

# SOLUTION 4:

SELECT sales.cust_id, order_id, delivery_status
FROM orders
JOIN sales
ON orders.cust_id = sales.cust_id
WHERE delivery_status = 'pending'
ORDER BY sales.cust_id,order_id;


/*

QUESTION 5: compare sales from todays date with previous date, all the sales happened on '2023-05-01' vs '2023-04-31'

Format of result : current_day_sale = sale on 2023-05-01 , previous_day_sale = sale on 2023-04-30 , sale difference. 

*/

# SOLUTION 5:

SELECT 
    SUM(order_amt) AS `Total sale on 2023-05-01`,
    LAG(SUM(order_amt),1,0) OVER (ORDER BY sale_date) AS `Total sale on 2023-04-30`,
    SUM(order_amt) - LAG(SUM(order_amt),1,0) OVER (ORDER BY sale_date) AS `sale difference`
FROM orders
JOIN sales 
ON orders.cust_id = sales.cust_id
GROUP BY sale_date
ORDER BY sale_date
LIMIT 1 OFFSET 1;
