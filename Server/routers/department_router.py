from flask import Blueprint,jsonify,request
from BLL.department_bl import *
from routers.auth_router import *

departments = Blueprint('departments',__name__)
departments_bl = DepartmentBL()

#get ALL
@departments.route("/", methods=['GET'])
def get_all_departments():
    is_join=request.args.get("is_join")

    departments = action_verify_token(departments_bl.get_all_departments,[is_join])
    return departments


@departments.route("/<id>",methods=['GET'])
def get_department(id):
    department_recv =action_verify_token(departments_bl.get_department,[id])
    return department_recv


@departments.route("/",methods=['POST'])
def add_department():
    obj = request.json
    resp = action_verify_token(departments_bl.add_department,[obj])
    return resp


@departments.route("/<id>",methods=['PUT'])
def update_department(id):
    obj=request.json
    resp = action_verify_token(departments_bl.update_department,[id,obj])
    return resp


@departments.route("/<id>",methods=['DELETE'])
def delete_department(id):
    resp = action_verify_token(departments_bl.delete_department,[id])
    return resp
