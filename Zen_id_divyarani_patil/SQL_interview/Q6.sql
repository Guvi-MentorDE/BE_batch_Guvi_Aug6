create TABLE if not exists accounts(
    id INT,
    name varchar(50),
    primary key (id)
);

create table if not exists logins(
    id INT,
    login_date date
);

insert INTO accounts VALUES(1,'winston'),(7,'jonathan');

insert into logins VALUES(7,' 2020-05-30'),
(1,'2020-05-30'),(7,' 2020-05-31'),(7,'2020-06-01'),(7,' 2020-06-02'),
(7,' 2020-06-02 '),(7,' 2020-06-03'),
(1,' 2020-06-07'),(7,' 2020-06-10');


----pending-----
select a.id , a.name from accounts a left join logins l on a.id = l.id where login_date