import pymongo


class MongoDataLayer:

    def __create(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwartsDB"]

    def __init__(self):
        self.__create()

    def get_all_users(self):
        user_dict = {}
        users = self.__db["users"].find({"smthing"})
        for user in users:
            user_dict[user["_id"]] = user

        return user_dict

