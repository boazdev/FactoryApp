from flask import Blueprint,jsonify,request, make_response
from BLL.employee_bl import *
from BLL.auth_bl import *
from routers.auth_router import *
employees = Blueprint('employees',__name__)
employees_bl = EmployeeBL()
auth_bl = AuthBL()


@employees.route("/", methods=['GET'])
def get_all_employees():
    is_join=request.args.get("is_join")

    employees = action_verify_token(employees_bl.get_all_employees,[is_join])

    return employees


@employees.route("/<id>",methods=['GET'])
def get_employee(id):
    is_shift=request.args.get("is_shift")

    employee_recv = action_verify_token(employees_bl.get_employee,[id,is_shift])
    return employee_recv


@employees.route("/",methods=['POST'])
def add_employee():
    obj = request.json

    resp = action_verify_token(employees_bl.add_employee,[obj])
    return resp


@employees.route("/<id>",methods=['PUT'])
def update_employee(id):
    obj=request.json

    resp = action_verify_token(employees_bl.update_employee,[id,obj])
    return resp


@employees.route("/<id>",methods=['DELETE'])
def delete_employee(id):

    resp = action_verify_token(employees_bl.delete_employee,[id])
    return resp
