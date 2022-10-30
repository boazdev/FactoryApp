from DAL.actions_file_dal import *
from datetime import datetime
from flask import g
class ActionBL:
    def __init__(self):
        self.__action_file_dal = ActionsFileDAL()

    def do_action(self):
        id = g.get("user_id")
        max_actions = g.get("user_max_actions")
        print("do_action doing action " + id +" " +str(max_actions))
        str_curr_date = str(datetime.today().date())
        actions_data = self.__action_file_dal.read_file()
        
        num_actions = len(list(filter(lambda x: x["id"]==id and x["date"]==str_curr_date,actions_data["actions"])))
        if num_actions == max_actions:
            print("user out of actions")
            return False
        print("num actions done today by user: " + str(num_actions))
        dict_action = {"id":id, "maxActions":max_actions, "date":str_curr_date, "actionsAllowd":max_actions-num_actions-1}
        actions_data["actions"].append(dict_action)
        self.__action_file_dal.write_file(actions_data)
        return True

    def get_num_actions_left(self,id,max_actions):
        str_curr_date = str(datetime.today().date())
        actions_data = self.__action_file_dal.read_file()
        num_actions = len(list(filter(lambda x: x["id"]==id and x["date"]==str_curr_date,actions_data["actions"])))
        return num_actions


        


