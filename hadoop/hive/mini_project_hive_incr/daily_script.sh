#!/bin/bash
exec_date=$1
file_path=/home/prera/data/emp_data_${exec_date}.txt
hive --hiveconf file_path="${file_path}" -f /home/prera/bin/scd.hql