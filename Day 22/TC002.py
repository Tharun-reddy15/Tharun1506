from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["Company_DB"]
collection = db["C1"]
result = collection.insert_one({"Name":"Tharun","Salary":10000})
result1 = collection.find({"Name":"Tharun"})
for data in result1:
    print(data)