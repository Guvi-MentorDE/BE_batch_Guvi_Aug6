create TABLE IF NOT EXISTS number(
    id INT,
    num INT
);

insert into number values(1,1),(2,1),(3,1),(4,2),(5,1),(6,2),(7,2);

SELECT max(num) as consectivenums from number;

SELECT num as consectivenums from number group by num having count(num)>1;