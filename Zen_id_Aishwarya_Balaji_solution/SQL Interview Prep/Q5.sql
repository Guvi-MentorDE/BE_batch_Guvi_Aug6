-- Table: Products

-- +------------------+---------+
-- | Column Name      | Type    |
-- +------------------+---------+
-- | product_id       | int     |
-- | product_name     | varchar |
-- | product_category | varchar |
-- +------------------+---------+
-- product_id is the primary key for this table.
-- This table contains data about the company's products.
-- Table: Orders

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | order_date    | date    |
-- | unit          | int     |
-- +---------------+---------+
-- There is no primary key for this table. It may have duplicate rows.
-- product_id is a foreign key to Products table.
-- unit is the number of products ordered in order_date.
 

-- Write an SQL query to get the names of products with greater than or equal to 100 units ordered in February 2020 and their amount.

-- Return result table in any order.

-- The query result format is in the following example:

 

-- Products table:
-- +-------------+-----------------------+------------------+
-- | product_id  | product_name          | product_category |
-- +-------------+-----------------------+------------------+
-- | 1           | Science Solutions    | Book             |
-- | 2           | Jewels of Stringology | Book             |
-- | 3           | HP                    | Laptop           |
-- | 4           | Lenovo                | Laptop           |
-- | 5           | Science Kit          | T-shirt          |
-- +-------------+-----------------------+------------------+

-- Orders table:
-- +--------------+--------------+----------+
-- | product_id   | order_date   | unit     |
-- +--------------+--------------+----------+
-- | 1            | 2020-02-05   | 60       |
-- | 1            | 2020-02-10   | 70       |
-- | 2            | 2020-01-18   | 30       |
-- | 2            | 2020-02-11   | 80       |
-- | 3            | 2020-02-17   | 2        |
-- | 3            | 2020-02-24   | 3        |
-- | 4            | 2020-03-01   | 20       |
-- | 4            | 2020-03-04   | 30       |
-- | 4            | 2020-03-04   | 60       |
-- | 5            | 2020-02-25   | 50       |
-- | 5            | 2020-02-27   | 50       |
-- | 5            | 2020-03-01   | 50       |
-- +--------------+--------------+----------+

-- Result table:
-- +--------------------+---------+
-- | product_name       | unit    |
-- +--------------------+---------+
-- | Science Solutions | 130     |
-- | Science Kit       | 100     |
-- +--------------------+---------+

-- Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
-- Products with product_id = 2 is ordered in February a total of 80.
-- Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
-- Products with product_id = 4 was not ordered in February 2020.
-- Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.

-- Solution

CREATE TABLE products 
(
    product_id INT, 
    product_name NVARCHAR(150), 
    product_category NVARCHAR(120), 
    CONSTRAINT PK PRIMARY KEY (product_id)
);

CREATE TABLE orders 
(
    product_id INT, 
    order_date DATE, 
    unit INT, 
    CONSTRAINT FK FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO products VALUES(1, 'Science Solutions', 'Book');
INSERT INTO products VALUES(2, 'Jewels of Stringology', 'Book');
INSERT INTO products VALUES(3, 'HP', 'Laptop');
INSERT INTO products VALUES(4, 'Lenovo', 'Laptop');
INSERT INTO products VALUES(5, 'Science Kit', 'T-shirt');


INSERT INTO orders VALUES(1, '2020-02-05', 60);
INSERT INTO orders VALUES(1, '2020-02-10', 70);
INSERT INTO orders VALUES(2, '2020-01-18', 30);
INSERT INTO orders VALUES(2, '2020-02-11', 80);
INSERT INTO orders VALUES(3, '2020-02-17', 2);
INSERT INTO orders VALUES(3, '2020-02-24', 3);
INSERT INTO orders VALUES(4, '2020-03-01', 20);
INSERT INTO orders VALUES(4, '2020-03-04', 30);
INSERT INTO orders VALUES(4, '2020-03-04', 60);
INSERT INTO orders VALUES(5, '2020-02-25', 50);
INSERT INTO orders VALUES(5, '2020-02-27', 50);
INSERT INTO orders VALUES(5, '2020-03-01', 50);

SELECT * FROM products;

SELECT * FROM orders;

SELECT DISTINCT val.* 
FROM 
(
    SELECT product_name, SUM(unit) OVER(PARTITION BY ord.product_id) AS unit 
    FROM products 
    INNER JOIN orders ord on ord.product_id = products.product_id AND MONTH(ord.order_date) = 2
) 
val 
where val.unit>=100;