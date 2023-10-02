#!/bin/bash
#exec_date=20230902
exec_date=$1
file_path=/home/prera/data/emp_data_${exec_date}.txt #make changes to this path according to your cluster folder structure
hive --hiveconf file_path="${file_path}" -f /home/prera/bin/scd.hql  #make changes to this path according to your cluster folder structure