from tkinter.messagebox import NO
import jwt
from DAL.user_ws_dal import UserWSDAL
from DAL.user_db_dal import UserDBDAL
from DAL.actions_file_dal import *
from flask import g
from datetime import datetime
#from BLL.action_bl import ActionBL
#from DAL.users_ws_dal import *
#from Server.DAL.users_ws_dal import UserWSDAL
class AuthBL:
    def __init__(self):
        self.__key = "server_key"
        self.__algorithm = "HS256"
        self.__user_ws_dal = UserWSDAL()
        self.__user_db_dal = UserDBDAL()
        self.__action_file_dal = ActionsFileDAL()
        

    def get_token(self,username,password):
        user_eid = self.__check_user(username,password)
        token = None
        print("get token user id: " + str(user_eid))
        user_id= None
        if user_eid!=None:
            user_recv = self.__user_db_dal.get_user_by_eid(user_eid)
            user_id =user_recv["_id"]
            user_max_actions = user_recv["NumOfActions"]
            num_left = self.get_num_actions_left(user_id,user_max_actions)
            if num_left == 0:
                return "out_of_actions"

        if user_eid is not None: 
            token = jwt.encode({"user_id" : str(user_id)},self.__key,self.__algorithm)
        return token


    def verify_token(self,token): 
        try:
            data = jwt.decode(token,self.__key,self.__algorithm)#,verify=True)
            user_id = data["user_id"]
            user_recv = self.__user_db_dal.get_user_by_id(user_id)
            if user_recv != None:
                g.setdefault("user_id",user_id)
                g.setdefault("user_max_actions",user_recv["NumOfActions"])
                return True
            else:
                return False
        except Exception as e:
            print("error:" + str(e) +" " +str(e.__traceback__))
            return False


    def __check_user(self,username,password): 
        user_obj = self.__user_ws_dal.get_user(username,password)
        if len(user_obj)>0:
            return user_obj[0]["id"]
        else:
            return None

    def get_num_actions_left(self,user_id, user_max_actions):
        actions_data = self.__action_file_dal.read_file()
        str_curr_date =str(datetime.today().date())
        num_actions = len(list(filter(lambda x: x["id"]==str(user_id) and x["date"]==str_curr_date,actions_data["actions"])))
        num_left= user_max_actions - num_actions
        print("users current number of actions on login: "+str(num_left))
        return num_left
