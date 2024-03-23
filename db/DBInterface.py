import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client["prostoXsberHack"]

collection = current_db["button"]
pylounge = {
    "text": "login"
}
result = collection.insert_one(pylounge)
print(result.inserted_id)
