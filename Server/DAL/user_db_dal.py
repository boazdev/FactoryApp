from pymongo import MongoClient
from bson import ObjectId
class UserDBDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factoryDB"]
        self.__collection = self.__db["users"]

    def get_user_by_eid(self,eid): #get user by external id retrieved from web service
        print("get user from db dal")
        user = self.__collection.find_one({"ExternalID":eid})
        return user
    
    def get_all_users(self):
        users = list(self.__collection.find({}))
        return users
    
    def get_user_by_id(self,id):
        user = self.__collection.find_one({"_id":ObjectId(id)})
        return user