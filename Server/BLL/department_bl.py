from DAL.department_db_dal import DepartmentDBDAL
from DAL.employee_db_dal import EmployeeDBDAL
from DAL.emp_to_shift_db_dal import EmpToShiftDBDAL
from bson import ObjectId
from BLL.action_bl import ActionBL
from flask import g
class DepartmentBL(ActionBL):
    def __init__(self):
        self.__department_db_dal = DepartmentDBDAL()
        self.__employee_db_dal = EmployeeDBDAL()
        self.__emp_to_shift_dal = EmpToShiftDBDAL()
        super(self.__class__,self).__init__()
        
    def get_all_departments(self,is_join):
        if is_join!=None:
            """ if super(self.__class__,self).do_action()==False:
                return False """
            pipeline = [
                            {"$lookup": {
                                    "from": "employees",
                                    "localField": "_id",
                                    "foreignField": "DepartmentID",
                                    "as": "deptEmps"
                                }
                                
                            },
                            {"$lookup": {
                                    "from": "employees",
                                    "localField": "Manager",
                                    "foreignField": "_id",
                                    "as": "deptManager"
                                }
                            }
                        ]
            depts = self.__department_db_dal.get_all_departments_aggr(pipeline)
            for d in depts:
                #d.pop("Manager")
                d["deptManager"]=d["deptManager"][0]["Firstname"] + " " +d["deptManager"][0]["Lastname"]
                #
            #print("departments join data:")
            #print(depts)
            departments=depts
        else:
            departments = self.__department_db_dal.get_all_departments()
        return departments
    
    def get_department(self,id):
        #print("get user bl")
        department = self.__department_db_dal.get_department(id)
        return department

    def add_department(self,obj):
        if super(self.__class__,self).do_action()==False:
                return False
        resp = self.__department_db_dal.add_department(obj)
        return resp

    def delete_department(self,id):
        if super(self.__class__,self).do_action()==False:
                return False
        resp = self.__department_db_dal.delete_department(id)
        pipeline = [
                    {"$match": {"DepartmentID": ObjectId(id)}}
                    ]       
        emps_del = self.__employee_db_dal.get_all_employees_aggr(pipeline)
        print("deleting employees data and shifts")
        
        for emp in emps_del:
            self.__emp_to_shift_dal.delete_emp_shifts(emp["_id"])
            self.__employee_db_dal.delete_employee(emp["_id"])
        
        return resp

    def update_department(self,id,obj):
        if super(self.__class__,self).do_action()==False:
                return False
        resp = self.__department_db_dal.update_department(id,obj)
        return resp
