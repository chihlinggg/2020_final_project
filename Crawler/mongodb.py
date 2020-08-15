from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydb = client["test"]
print(client.list_database_names())