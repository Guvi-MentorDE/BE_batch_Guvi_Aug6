drop table wc;
create table wc 
(word string
) 
stored as textfile;

load data local inpath '/home/Raj/data/hive_data/workcount.txt' into table wc;


select word, count(*) 
from(
select explode(split(word,',')) as word
from wc
)t
group by word
;