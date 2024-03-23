import pymongo


class DBInterface:

    def add_button(self):
        db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        current_db = db_client["prostoXsberHack"]
        collection = current_db["button"]
        pylounge = {
            "text": "login"
        }
        result = collection.insert_one(pylounge)
        print(result.inserted_id)


    def getUserLogPassByID(self, user_id):
        db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        current_db = db_client["prostoXsberHack"]
        collection = current_db["user"]
        result = collection.find_one({"id": user_id})

        if not result:
            print('Пользователь не найден')
            return None
        return result
