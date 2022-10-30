from pymongo import MongoClient
from bson import ObjectId
class DepartmentDBDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factoryDB"]
        self.__collection = self.__db["departments"]

    def get_department(self,id): #get department by object id retrieved from database
        print("get department from db dal")
        department = self.__collection.find_one({"_id":ObjectId(id)})
        return department
    
    def get_all_departments(self):
        departments = list(self.__collection.find({}))
        return departments
    
    def get_all_departments_aggr(self,pipeline):
        departments = list(self.__collection.aggregate(pipeline))
        return departments
    
    def add_department(self,obj):
        obj["Manager"] = ObjectId(obj["Manager"])
        self.__collection.insert_one(obj)
        return "Created department with ID " +str(obj["_id"])


    def delete_department(self,id):
        self.__collection.delete_one({"_id":ObjectId(id)})
        return "Deleted department!"

    def update_department(self,id,obj):
        if (obj.get("Manager")!=None):
            obj["Manager"] = ObjectId(obj["Manager"])
        self.__collection.update_one({"_id": ObjectId(id)},{"$set":obj})
        return "Updated department"