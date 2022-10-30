from DAL.user_db_dal import *
from flask import g
from BLL.action_bl import ActionBL
from DAL.actions_file_dal import *
from datetime import datetime
class UserBL(ActionBL):
    def __init__(self):
        self.__user_db_dal = UserDBDAL()
        self.__actions_file_dal = ActionsFileDAL()
        super(self.__class__,self).__init__()

    def get_users(self):
        """ if super(self.__class__,self).do_action()==False:
                return False """
        users_file_data = self.__actions_file_dal.read_file()
        users_file_lst = users_file_data["actions"]
        
        users = self.__user_db_dal.get_all_users() # also get remaining actions
        str_curr_date = str(datetime.today().date())
        for user in users:
            num_actions = len(list(filter(lambda x: x["id"]==str(user["_id"]) and str(x["date"])==str_curr_date,users_file_lst)))
            user["currActions"] = user["NumOfActions"] - num_actions
        return users
    
    def get_user_by_eid(self,eid):
        print("get user bl")
        user = self.__user_db_dal.get_user(int(eid))
        return user

    def get_user_by_id(self,id):
        user_recv = self.__user_db_dal.get_user_by_id(id)
        return user_recv