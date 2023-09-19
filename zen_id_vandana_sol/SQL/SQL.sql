"""
#question 1 {find the country which has 3 most highest no of orders ?  //solve:
result : country , orders 
sol
"""
mysql> select count(country) as no_of_orders,country
    -> from orders
    -> group by country
    -> order by count(country) desc
    -> ;
+--------------+---------+
| no_of_orders | country |
+--------------+---------+
|            4 | USA     |
|            4 | india   |
|            1 | UK      |
+--------------+---------+
"""
#question 3 sol
provide ranking for the countries based on the total amount of order. 
result : rank, country, total amount  of orders. 
"""""
mysql> select country,
    -> sum(order_amt) as total_order_amt,
    -> rank() over (order by sum(order_amt) desc) as country_rank
    -> from orders
    -> group by country
    -> order by total_order_amt desc;
+---------+-----------------+--------------+
| country | total_order_amt | country_rank |
+---------+-----------------+--------------+
| india   |           61300 |            1 |
| USA     |           49900 |            2 |
| UK      |           13000 |            3 |
+---------+-----------------+--------------+
"""
#question 2 {sum of order amounts for each country.
result ; country , sum of order amounts. } 
"""

 select sum(order_amt),country
    -> from orders
    -> group by country;
+----------------+---------+
| sum(order_amt) | country |
+----------------+---------+
|          49900 | USA     |
|          61300 | india   |
|          13000 | UK      |
+----------------+---------+
"""
Question 4:join sales vs orders. 
find the orders that are still pedning to be delivered 
"""
select sale_date,delivery_status,order_id,country,state,order_amt
    -> from sales as s
    -> join orders as o on s.cust_id=o.cust_id
    -> where delivery_status="pending";
+------------+-----------------+----------+---------+---------+-----------+
| sale_date  | delivery_status | order_id | country | state   | order_amt |
+------------+-----------------+----------+---------+---------+-----------+
| 2023-05-01 | pending         |      100 | USA     | Seattle |     10000 |
| 2023-04-30 | pending         |      109 | UK      | London  |     13000 |
| 2023-05-01 | pending         |      120 | India   | AP      |      2000 |
| 2023-05-01 | pending         |      131 | USA     | Seattle |      6900 |
+------------+-----------------+----------+---------+---------+-----------+
"""
Question 5: compare sales from todays date with previous date. 
all the sales happened on '2023-05-01' vs '2023-04-31'
result : current row , previous date , diff. 
"""

