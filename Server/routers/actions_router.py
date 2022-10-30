from flask import Blueprint,jsonify,request
from BLL.action_bl import *
from routers.auth_router import *

actions = Blueprint('actions',__name__)
actions_bl = ActionBL()

@actions.route("/",methods=['POST'])
def add_action():
    resp = action_verify_token(actions_bl.do_action)
    return resp