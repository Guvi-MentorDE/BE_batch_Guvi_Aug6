#!/bin/bash

#exec_date=20230902
exec_date=$1

file_path=/home/Raj/data/hive_data/emp_data_${exec_date}.txt #20230902

hive --hiveconf file_path="${file_path}" -f /home/Raj/bin/scd.hql
