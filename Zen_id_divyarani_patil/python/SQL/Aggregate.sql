CREATE TABLE IF NOT EXISTS store(
    sales_date date,
    shop_id varchar(50),
    sales_amt int
);

insert into store VALUES('2020-12-06','S1',200);
insert into store VALUES('2021-05-06','S3',400);
insert into store VALUES('2022-02-12','S1',500);
insert into store VALUES('2020-12-06','S2',700);
insert into store VALUES('2020-12-06','S2',300);
insert into store VALUES('2020-12-06','S3',800);
insert into store VALUES('2020-12-06','S2',400);
insert into store VALUES('2020-12-06','S3',600);

SELECT * from store;

select *, sum(sales_amt) over(ORDER BY shop_id ) as running_sum_of_sales
from store;

select * , avg(sales_amt) OVER(ORDER BY shop_id DESC) as average_sales
from store;

SELECT * , sum(sales_amt) OVER(PARTITION BY shop_id) as total
from store;

SELECT *, min(sales_amt) OVER(PARTITION BY shop_id ) AS total
FROM store; 

