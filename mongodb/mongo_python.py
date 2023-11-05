import pymongo
from pymongo import MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["flights"]

print(mydb)
print("display db names")
print(myclient.list_database_names())


print("create collection")
mycol = mydb["flights_new"]


print("insert operation")

record=[
  {
    "departureAirport": "MUC",
    "arrivalAirport": "SFO",
    "aircraft": "Airbus A380",
    "distance": 12000,
    "intercontinental": "true"
  },
  {
    "departureAirport": "LHR",
    "arrivalAirport": "TXL",
    "aircraft": "Airbus A320",
    "distance": 950,
    "intercontinental": "false"
  } 
]

rec = mydb.flights_new.insert_many(record)  

print("retriving the records")

#for i in mydb.flights_new.find({"intercontinental": 'false'}):
#    print(i) 

print("retrive using cursor")
collection = mydb.flights_new 

print("update the records")
    
updt=collection.update_many( {"distance": 12000}, { "$set": {"status":"update"}})

cursor = collection.find()
for record in cursor: 
    print(record) 
    
    
print("delete")

myquery = { "status": "update" }

delete = collection.delete_one(myquery)


cursor = collection.find() 
for record in cursor: 
    print(record) 
    
    
collection.drop()