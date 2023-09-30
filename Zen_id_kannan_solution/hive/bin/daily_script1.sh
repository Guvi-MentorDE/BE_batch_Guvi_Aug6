#!/bin/bash
#exec_date=20230901
exec_date=$1
file_path=/home/kanna/data/datasetup/emp_data_${exec_date}.txt
hive --hiveconf file_path="${file_path}" -f /home/kanna/bin/scd_typ2.hql