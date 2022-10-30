from DAL.employee_db_dal import *
from DAL.emp_to_shift_db_dal import *
from flask import g
from BLL.action_bl import ActionBL
class EmployeeBL(ActionBL):
    def __init__(self):
        self.__employee_db_dal = EmployeeDBDAL()
        self.__emp_to_shift_dal = EmpToShiftDBDAL()
        super(self.__class__,self).__init__()

    def get_all_employees(self,is_join): 
        if is_join!=None:
            """ if super(self.__class__,self).do_action()==False:
                return False """
            emp_pipeline = [
                {
                    "$lookup":
                    {
                        "from": "departments",
                        "localField": "DepartmentID",
                        "foreignField": "_id",
                        "as": "departmentData"
                    }
                    
                }, {"$unwind":"$departmentData"},
                
                {   
            "$project":{
                "_id" : 1,
                "Firstname" : 1,
                "Lastname" : 1,
                "DepartmentID" : 1,
                "departmentName" : "$departmentData.Name",
                
            } 
            }]
            shift_pipeline = [
                {
                    "$lookup": {
                    "from": "departments",
                    "localField": "DepartmentID",
                    "foreignField": "_id",
                    "as": "empDept"
                }
                }, {"$unwind" : "$empDept"},
                
                {   
                "$lookup": {
                    "from": "employeesToShifts",
                    "localField": "_id",
                    "foreignField": "empID",
                    "as": "empShifts"
                }
                },{
                "$unwind" : "$empShifts"
                },{
                "$lookup" : {
                    "from" : "shifts",
                    "localField" : "empShifts.shiftID",
                    "foreignField" : "_id",
                    "as" : "shiftdata"
                }
                },{
                "$unwind" : "$shiftdata"
                },{
                "$group" : {
                    "_id" : "$_id",
                    "shiftDate" : {"$push" : "$shiftdata"}
                }}]
            

            employees_dept = self.__employee_db_dal.get_all_employees_aggr(emp_pipeline)
            employees_shifts = self.__employee_db_dal.get_all_employees_aggr(shift_pipeline)
            #print(employees_shifts)
            for empdept in employees_dept:
                lst_filt= list(filter(lambda x: x["_id"]==empdept["_id"],employees_shifts))
                if len(lst_filt)>0:
                    empdept["shifts"] = lst_filt[0]
                else:
                    empdept["shifts"] = None
           
            employees= employees_dept
        else:
            employees = self.__employee_db_dal.get_all_employees()
        return employees
    
    def get_employee(self,id,is_shift):
       
        if is_shift!= None:
            shift_pipeline = [
                {
                    "$lookup": {
                    "from": "departments",
                    "localField": "DepartmentID",
                    "foreignField": "_id",
                    "as": "empDept"
                }
                }, {"$unwind" : "$empDept"},
                
                {   
                "$lookup": {
                    "from": "employeesToShifts",
                    "localField": "_id",
                    "foreignField": "empID",
                    "as": "empShifts"
                }
                },{
                "$unwind" : "$empShifts"
                },{
                "$lookup" : {
                    "from" : "shifts",
                    "localField" : "empShifts.shiftID",
                    "foreignField" : "_id",
                    "as" : "shiftdata"
                }
                },{
                "$unwind" : "$shiftdata"
                },{
                "$group" : {
                    "_id" : "$_id",
                    "shiftDate" : {"$push" : "$shiftdata"}
                }},
                {
                    "$match" : {   "_id":  ObjectId(id)}
                    
                    
                }]
            employee_shifts = self.__employee_db_dal.get_employee_aggr(shift_pipeline)
            print(employee_shifts)
            if len(employee_shifts)>0:
                employee = employee_shifts[0]
            else: 
                employee = None
        else:
            employee = self.__employee_db_dal.get_employee(id)

        return employee

    def add_employee(self,obj):
        if super(self.__class__,self).do_action()==False:
                return False
        resp = self.__employee_db_dal.add_employee(obj)
        return resp

    def delete_employee(self,id):
        if super(self.__class__,self).do_action()==False:
                return False
        resp_one = self.__emp_to_shift_dal.delete_emp_shifts(id)
        resp = self.__employee_db_dal.delete_employee(id)
        
        return resp

    def update_employee(self,id,obj):
        shift_id = obj.get("sID")
        if super(self.__class__,self).do_action()==False:
                return False
        print("update employee bl:")
        print("shift id: " +str(shift_id))
        print("update item: ")
        print(obj)
        obj.pop("sID")
        if(shift_id!=None):
            
            shift_obj = { "empID":id, "shiftID": shift_id}
            resp2 = self.__emp_to_shift_dal.add_emp_to_shift(shift_obj)
 
        resp = self.__employee_db_dal.update_employee(id,obj)
        return resp
