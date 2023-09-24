--this is a daily load table : contains only current day records -----
create database if not exists incr_load;
use incr_load;

drop table incr_load.emp_raw_daily_table;
create table if not exists incr_load.emp_raw_daily_table 
(emp_name string,
sal int,
txn_data date
) 
row format delimited fields terminated by',' lines terminated by'\n'
stored as textfile;

load data local inpath '${hiveconf:file_path}' into table incr_load.emp_raw_daily_table; 

--- final master table -----
create external table if not exists incr_load.emp_master 
(emp_name string,
sal int
) 
partitioned by(txn_data date)
row format delimited fields terminated by',' lines terminated by'\n'
stored as textfile;

--- staging ---------------------
drop table incr_load.emp_temp;
create table if not exists incr_load.emp_temp 
(emp_name string,
sal int,
txn_data date
) 
row format delimited fields terminated by',' lines terminated by'\n'
stored as textfile;

insert into table incr_load.emp_temp
select emp_name , sal, txn_data from incr_load.emp_raw_daily_table;

insert into table incr_load.emp_temp
select emp_name , sal, txn_data from incr_load.emp_master;

---------- insert into final master ------------

insert overwrite table incr_load.emp_master
select emp_name, sal , txn_data
from(
select row_number() over(partition by a.emp_name order by a.txn_data desc) rnum , emp_name, sal , txn_data 
from incr_load.emp_temp a)x
where rnum = 1;