import pymongo
from werkzeug.security import generate_password_hash


class DBInterface:
    # db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    # current_db = db_client["prostoXsberHack"]
    # collection = current_db["user"]
    # pylounge = {
    #     "name": "asa",
    #     "password": "scrypt:32768:8:1$q0HgyABsMdpcMlgT$d39836fbc6a437f549a16a1b9ce0e9ce65173cf4d32969afa2c698841502d4126a81412d3b72b8b72ec49cba20e34f48b98e589f7abe771df832de6c53a5cf62",
    #     "role": "1"
    # }
    # result = collection.insert_one(pylounge)
    # print(result.inserted_id)

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

    def getUserByLogin(self, username):
        db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        current_db = db_client["prostoXsberHack"]
        collection = current_db["user"]
        result = collection.find_one({"username": username})

        if not result:
            print('Пользователь не найден')
            return None
        return result

    def addUser(self, form):
        try:
            hash_password = generate_password_hash(form["password"])

            db_client = pymongo.MongoClient("mongodb://localhost:27017/")
            current_db = db_client["prostoXsberHack"]
            collection = current_db["user"]
            pylounge = {
                "username": form["username"],
                "password": hash_password,
                "name": form["name"],
                "lastname": form["lastname"]
            }
            result = collection.insert_one(pylounge)
            print(result)

            print("Пользователь успешно добавлен")
            return True
        except:
            print("При добавлении пользователя возникла ошибка")
            return False


    def getTrack(self):
        db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        current_db = db_client["prostoXsberHack"]
        collection = current_db["tracks"]
        result = collection.find()
        return result
