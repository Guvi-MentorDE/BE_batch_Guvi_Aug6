# BE_batch_Guvi_Aug6
Python Class Notes.

Install SQL workbench: {for AUG 17 class}
Download from ->
https://dev.mysql.com/downloads/workbench/

Installation steps on YT video 

-> https://www.youtube.com/watch?v=u96rVINbAUI



mYSQL REFERENCE MANUAL : https://dev.mysql.com/doc/refman/8.0/en/join.html


Refer for books and documents:

https://drive.google.com/drive/folders/1qJnUbeXwjIIPSv8LuO7_g4Ofeaf5Qbjf


We shall be using GCP for practise of Hadoop , Hive and Spark. Since GCP is going to offer 25K credits for 90 days best amount existing cloud providers. 

Instructions for Creating Hadoop cluster:

1) Enable your Free trial account account. [login into console.google.cloud]

2) Enabe your Dataproc API & storage API service. 

3) go to Dataproc -> create cluster -> login via ssh 

4) start using linux , hadoop , hive , spark. 


Follow the video to setup google cloud cli:
-----------------------------------------------
https://www.youtube.com/watch?v=7mE-9E4D4Os



Handelling Source code from Git to Hadoop Cluser:
--------------------------------------------------

Since many people are facing issues with respect to spacing in project execution. We can avoid copy pasting going forward. 


1) login into dataproc cluster.
2) do cd ~
3) sudo apt install git-all   [run the command] -> once done -> verify using -> git --version command.
4) create some directory of your choice and run "git clone https://github.com/Guvi-MentorDE/BE_batch_Guvi_Aug6.git"

lets not copy past or move to google cloud bucket going forward unless its necessary. 


**Setup local cloudera onpremise 1 node cluser:**
Please follow the below video for clarity
https://www.youtube.com/watch?v=nTzgeTKQg2E&t=419s



Semi Strcutred and unstructred project datasets are available in below google drive:
https://drive.google.com/file/d/1GQQ3NfedinizkKHhER979ixhbhVNXXN_/view?usp=sharing
copy to your GCS bucket and cluster. 


MongoDb installation:
-----------------------
https://www.mongodb.com/try/download/community -> choose -> version 5.0.22
install -> custom mode 
once done -> copy the path from path from C drive and paste in your "PATH" of System variables.
create a folder structures as : C -> data -> db 
start your server : mongod ( in new cmd prompt)
start your client : mongo (in new cmd promt)


Google drive from class notes (temp)
https://drive.google.com/drive/folders/1JG_s3QtjRby4kAmQqepzwVUAEBz6mRJR?usp=sharing
