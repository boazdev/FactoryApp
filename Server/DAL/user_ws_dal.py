import requests

class UserWSDAL:
    def __init__(self):
        self.__url = "https://jsonplaceholder.typicode.com/users"

    def get_user(self,username,password): 
        obj={"username":username,"email":password}
        print("Before dal ws request get")
        resp=requests.get(self.__url,obj) 
        print("After dal ws request get")
        return resp.json()



