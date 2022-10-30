from flask import Blueprint,jsonify,request, make_response
#from BLL.user_bl import UserBL
from BLL.user_bl import *
from routers.auth_router import *
users = Blueprint('users',__name__)
users_bl = UserBL()


@users.route("/", methods=['GET'])
def get_all_users():
    users_recv = action_verify_token(users_bl.get_users)
    return users_recv


@users.route("/<id>",methods=['GET'])
def get_user(id):
    user_recv = action_verify_token(users_bl.get_user_by_id,[id])
    return user_recv
