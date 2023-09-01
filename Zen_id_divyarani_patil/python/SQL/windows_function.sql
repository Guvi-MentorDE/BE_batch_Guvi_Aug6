SELECT *, sum(sales_amt) OVER(PARTITION BY shop_id)as total
from store;

SELECT *, sum(sales_amt) OVER(PARTITION BY shop_id ORDER BY sales_date) as total
from store;

SELECT *, sum(sales_amt) OVER(PARTITION BY shop_id ORDER BY sales_date) as total,
max(sales_amt) OVER(PARTITION BY shop_id ORDER BY sales_date) as maxi,
avg(sales_amt) OVER(PARTITION BY shop_id ORDER BY sales_date) as aver,
min(sales_amt) OVER(PARTITION BY shop_id ORDER BY sales_date) as mini
from store
limit 4;

create TABLE IF NOT EXISTS sale_table(
    sales_date date,
    sales_amount int
);

insert INTO sale_table VALUES('2020-02-15',500);
insert INTO sale_table VALUES('2021-03-14',900);
insert INTO sale_table VALUES('2021-09-03',400);
insert INTO sale_table VALUES('2022-06-15',800);
insert INTO sale_table VALUES('2022-10-16',100);
insert INTO sale_table VALUES('2021-11-20',700);
insert INTO sale_table VALUES('2021-05-05',300);
insert INTO sale_table VALUES('2020-12-03',400);

select * FROM sale_table;

SELECT *, avg(sales_amount) OVER(ORDER BY sales_date) as roll_avg from sale_table;

SELECT * FROM store;


select ROW_NUMBER() OVER(PARTITION BY shop_id ORDER BY sales_amt DESC) as row_num
from store;

SELECT RANK() OVER(PARTITION BY shop_id ORDER BY sales_amt DESC) as rank_val
from store;

SELECT DENSE_RANK() OVER(PARTITION BY shop_id ORDER BY sales_amt DESC) as dense_val
from store;

SELECT *, ROW_NUMBER() OVER(PARTITION BY shop_id ORDER BY sales_amt DESC) as row_num,
rank() OVER(PARTITION BY shop_id ORDER BY sales_amt DESC) as rank_val,
DENSE_RANK() OVER(PARTITION BY shop_id ORDER BY sales_amt DESC) as dense_val
from store;

select tmp.*,
FROM(SELECT * , rank() OVER(PARTITION BY dept_name ORDER BY salary DESC) as rank_num from employees)tmp
where tmp.rank_num = 1;