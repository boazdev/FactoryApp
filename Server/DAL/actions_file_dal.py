import os
import json
import sys

class ActionsFileDAL:
    def __init__(self):
        self.__path = os.path.join(sys.path[0],'data/actions_log.json')

    def read_file(self):
        f = open(self.__path,'r')
        data = json.load(f)
        f.close()
        return data

    def write_file(self,data):
        f = open(self.__path,'w')
        json.dump(data,f,indent=4)
        f.close()