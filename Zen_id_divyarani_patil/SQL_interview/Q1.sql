

create TABLE IF NOT EXISTS author (
    article_id INT,
    author_id INT,
    viewer_id INT,
    view_date INT
);

alter table author modify column view_date date;

INSERT INTO author VALUES 
(1 , 3 ,5,'2019-08-01'),
(1,3,6,'2019-08-02'),
(2,7,7,'2019-08-01'),
(2,7,6,'2019-08-02'),
(4,7,1,'2019-07-22'),
(3,4,4,'2019-07-21'),
(3,4,4,'2019-07-21');

select distinct author_id as id from author 
where author_id = viewer_id order by author_id asc;



