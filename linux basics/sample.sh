#!/bin/bash 

now=$(date +"%T")
echo "Current time : $now"  >> /home/Raj/bin/logs/temp.txt

echo "**end of execution**"


# */1 * * * * /home/Raj/bin/sample.sh

crontab -l