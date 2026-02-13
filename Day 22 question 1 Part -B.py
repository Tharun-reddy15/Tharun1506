from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]

# Insert
collection.insert_one({
    "name": "tharun",
    "department": "IT",
    "salary": 90000
})

# Find IT employees
for emp in collection.find({"department": "IT"}):
    print(emp)

# Update salary
collection.update_one(
    {"name": "tharun"},
    {"$set": {"salary": 95000}}
)

print("Updated successfully!")