CREATE TABLE IF NOT EXISTS prog(
    program_date TIMESTAMP,
    content_id int,
    channel VARCHAR(50)
);

INSERT INTO prog VALUES('2020-06-10 08:00',1 ,'lc-channel'),
('2020-05-11 12:00',2 ,'lc-channel'),
('2020-05-12 12:00',3 ,'lc-channel'),
('2020-05-13 14:00',4 ,'disney ch'),
('2020-06-18 14:00',4 ,'disney ch'),
('2020-07-15 16:00',5 ,'disney ch');


create TABLE IF NOT EXISTS content(
    content_ids int,
    title VARCHAR(50),
    kids_content VARCHAR(50),
    content_type VARCHAR(50)
);

INSERT INTO content VALUES(1,'sciencefiction movie','N','movies'),
(2,'alg for kids','Y','Series'),
(3,'Database sols ','N','Series'),
(4,'Aladdin ','N','movies'),
(5,'Cinderella ','Y','movies');

SELECT DISTINCT title from content JOIN prog on prog.content_id = content.content_id 
where kids_content = 'Y' and date_format(program_date , '%Y-%m') ='2020-06' 
and content_type= 'movies';
