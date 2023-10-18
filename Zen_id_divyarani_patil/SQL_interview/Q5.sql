CREATE TABLE IF NOT EXISTS products(
    product_id INT,
    product_name VARCHAR(50),
    product_category VARCHAR(50),
    primary key (product_id)
    );
create table if not exists orders(
	product_id int,
    order_date date,
    unit int
);

insert into products values (1,'science solutions','book'),
(2,'jewels of stringology','book'),
(3,'hp','laptop'),
(4,'lenovo','laptop'),
(5,'science kit','t-shirt');

insert into orders values(1,'2020-02-05',60),
(1,'2020-02-10 ',70),
(2,'2020-01-18',30),
(2,' 2020-02-11 ',80),
(3,'2020-02-17 ',2),
(3,'2020-02-24',3),
(4,'2020-03-01',20),
(4,'2020-03-04',30),
(4,'2020-03-04 ',60),
(5,'2020-02-25 ',50),
(5,' 2020-02-27',50),
(5,'2020-03-01',50);


select p.product_name , sum(unit) as unit from products p
left join orders o on p.product_id = o.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_id
having sum(unit)>=100