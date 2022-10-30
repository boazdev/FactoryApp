from pymongo import MongoClient
from bson import ObjectId

class EmpToShiftDBDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factoryDB"]
        self.__collection = self.__db["employeesToShifts"]

    def get_emp_to_shift(self,id): #get 
        emp_to_shift_record = self.__collection.find_one({"_id":ObjectId(id)})
        return emp_to_shift_record
    
    def get_all_emp_to_shifts(self):
        emp_to_shift_lst = list(self.__collection.find({}))
        return emp_to_shift_lst
        

    def add_emp_to_shift(self,obj):
        obj["empID"] = ObjectId(obj["empID"])
        obj["shiftID"] = ObjectId(obj["shiftID"])
        self.__collection.insert_one(obj)
        return "Created employee to shift record with ID " +str(obj["_id"])

    def delete_emp_to_shift(self,id):
        self.__collection.delete_one({"_id":ObjectId(id)})

    
    def delete_emp_shifts(self,empID):
        self.__collection.delete_many({"empID":ObjectId(empID)})
        return "Deleted employee " +str(empID) +" " +"shifts"
    
    def update_emp_to_shift(self,id,obj): 
        pass