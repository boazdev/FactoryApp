from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
class ShiftDBDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factoryDB"]
        self.__collection = self.__db["shifts"]

    def get_shift(self,id): #get shift by object id retrieved from database
        print("get shift from db dal")
        shift = self.__collection.find_one({"_id":ObjectId(id)})
        return shift
    
    def get_all_shifts(self):
        shifts = list(self.__collection.find({}))
        return shifts
    
    def get_all_shifts_existing(self):
        shifts = list(self.__collection.find({ "Date": { 
        "$gte":  datetime.today()

      } }))
        return shifts
    
    def add_shift(self,obj):
        datetime_obj = datetime.strptime(obj["Date"], '%Y-%m-%d')
        obj["Date"] = datetime_obj
        self.__collection.insert_one(obj)
        return "Created shift with ID " +str(obj["_id"])


    def update_shift(self,id,obj): 
        datetime_obj = datetime.strptime(obj["Date"], '%Y-%m-%d')
        obj["Date"] = datetime_obj
        self.__collection.update_one({"_id": ObjectId(id)},{"$set":obj}) 
        return "Updated shift"