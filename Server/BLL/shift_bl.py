from DAL.shift_db_dal import *
from DAL.emp_to_shift_db_dal import *
from BLL.action_bl import ActionBL
from flask import g
class ShiftBL(ActionBL):
    def __init__(self):
        self.__shift_db_dal = ShiftDBDAL()
        self.__emp_to_shift_db_dal = EmpToShiftDBDAL()
        super(self.__class__,self).__init__()

    def get_all_shifts(self,is_existing=None):
        if is_existing == "true":
            shifts = self.__shift_db_dal.get_all_shifts_existing()
        else:
            shifts = self.__shift_db_dal.get_all_shifts()     
        return shifts
    
    def get_shift(self,id):
        shift = self.__shift_db_dal.get_shift(id)
        return shift

    def add_shift(self,obj):
        if super(self.__class__,self).do_action()==False:
                return False
        resp = self.__shift_db_dal.add_shift(obj)
        return resp

   

    def update_shift(self,id,obj):
        if super(self.__class__,self).do_action()==False:
                return False
        emp_id = obj.get("empID")
        if emp_id!=None:
            resp = self.__emp_to_shift_db_dal.add_emp_to_shift(obj)
        else:
            resp = self.__shift_db_dal.update_shift(id,obj)
        return resp
