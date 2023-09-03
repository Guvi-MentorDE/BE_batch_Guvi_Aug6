create TABLE cust(
    cust_id INT,
    cust_name varchar(50),
    primary key (cust_id)
);

insert into cust values(10 , 'michael');
insert into cust values(11 , 'Jordan');

create TABLE ordering(
    order_id INT,
    c_id INT,
    constraint pk primary key (order_id),
    constraint fi foreign key (c_id) references cust(cust_id)
);

insert INTO ordering VALUES (1001 , 10);

SELECT * FROM ordering; 

CREATE TABLE payment(
    pay_amt DECIMAL(8,2),
    pay_date date,
    store_id int
);

insert into payment VALUES
(125.36 , '2020-11-10' ,1),
(1025.36, '2021-02-11' , 2),
(1041.25,'2022-03-15',1),
(958.25,'2022-06-12',2),
(693.36,'2020-05-14',3),
(256.36,'2021-05-11',3),
(5896.36,'2020-03-17',1),
(8953.36,'2021-06-11',2),
(5658.36,'2022-05-17',1),
(874.69,'2023-02-12',2),
(698.37,'2021-02-11',3);

select year(pay_date) as 'payment year',
month(pay_date) as 'payment month',
store_id as 'store'
from payment;

select sum(pay_amt),year(pay_date) as 'payment year',
store_id as 'store'
from payment 
GROUP BY YEAR(pay_date),store_id with rollup
order BY year(pay_date),store_id;

select sum(pay_amt) , year(pay_date) as 'payment year'
from payment 
group by year(pay_date)
order by year(pay_date);