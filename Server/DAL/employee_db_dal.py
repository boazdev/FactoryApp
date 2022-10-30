from pymongo import MongoClient
from bson import ObjectId
class EmployeeDBDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factoryDB"]
        self.__collection = self.__db["employees"]

    def get_employee(self,id): 
        print("get employee from db dal")
        employee = self.__collection.find_one({"_id":ObjectId(id)})
        return employee

    def get_employee_aggr(self,pipeline):
        employee = self.__collection.aggregate(pipeline)
        return list(employee)

    def get_all_employees_aggr(self,pipeline):
        employees_data = self.__collection.aggregate(pipeline)
        return list(employees_data)
    
    def get_all_employees(self):
        employees = list(self.__collection.find({}))
        return employees
    
    def add_employee(self,obj):
        obj["DepartmentID"] = ObjectId(obj["DepartmentID"])
        self.__collection.insert_one(obj)
        return "Created employee with ID " +str(obj["_id"])


    def delete_employee(self,id):
        self.__collection.delete_one({"_id":ObjectId(id)})
        return "Deleted employee!"

    def update_employee(self,id,obj):
        if (obj.get("DepartmentID")!=None):
            obj["DepartmentID"] = ObjectId(obj["DepartmentID"])        
        self.__collection.update_one({"_id": ObjectId(id)},{"$set":obj})
        return "Updated Employee"