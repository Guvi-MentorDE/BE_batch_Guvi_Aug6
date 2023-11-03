#exec_date=20230902
exec_date=$1
file_path=/home/Dell/data/hive_datas/emp_data_${exec_date}.txt 
hive --hiveconf file_path="${file_path}" -f /home/Dell/bin/scdtype.hql