
from flask import Blueprint,jsonify, request, make_response

from flask import g
from BLL.auth_bl import AuthBL

auth = Blueprint('auth', __name__)

auth_bl = AuthBL()


@auth.route("/login", methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]

    token = auth_bl.get_token(username,password)
    if token == "out_of_actions":
        return make_response({"error" : "User out of actions" },401)
        
    if token is not None:
        return make_response({"token" : token},200)
    else:
        return make_response({"error" : "You're not authorized" },401)

def action_verify_token(func,arg="default"):
    if request.headers and request.headers.get('x-access-token'):
        token = request.headers.get('x-access-token')
        exist = False        
        exist = auth_bl.verify_token(token)

        if exist == True:
            if arg!="default":
                resp = func(*arg)
            else:
                resp = func()
            if resp==False:
                return make_response({"error": "Out of actions"},401)
            return jsonify(resp)

        else:
            return make_response({"error" : "Not authorized"},401)
    else:
        return make_response({"error" : "No token provided"},401)