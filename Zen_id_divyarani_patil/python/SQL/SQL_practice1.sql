create table IF NOT EXISTS carter(
    order_id int,
    cust_id int,
    order_date date,
    shipper_id int
);

create table customers(
    cust_id int,
    cust_name varchar(50),
    country varchar(50)
);

create table shippers(
    ship_id int,
    shipper_name varchar(50)
);

insert into carter values(1030 , 1 , '2020-12-20',3);
insert into carter values(1031 , 2 , '2020-08-10',4);
insert into carter values(1039 , 3 , '2020-09-11',5);
insert into carter values(1040 , 4 , '2020-10-09',6);
insert into carter values(1039 , 5 , '2020-01-08',2);

select * from carter;

insert into customers values(1 , 'alle','morrcco');
insert into customers values(2 , 'alan ','America');
insert into customers values(3 , 'bob','India ');
insert into customers values(4 , 'charlie','New zealand');
insert into customers values(5 , 'daniel','Australia ');

select * from customers;

insert into shippers values(1 , 'landers');
insert into shippers values(2 , 'Rogers ');

select * from shippers;

SELECT ca.* , c.*
from carter ca
INNER JOIN customers c ON ca.cust_id = c.cust_id;

select ca.* , c.*
from carter ca
LEFT JOIN customers c on ca.cust_id = c.cust_id;

SELECT ca.* , c.* FROM carter ca
RIGHT JOIN customers c on ca.cust_id = c.cust_id;

SELECT ca.* ,c.*,s.*
FROM carter ca
INNER JOIN customers c ON c.cust_id=ca.cust_id
INNER JOIN shippers s ON s.ship_id = ca.shipper_id;

