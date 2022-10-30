from flask import Blueprint,jsonify,request
from BLL.shift_bl import *
from routers.auth_router import *

shifts = Blueprint('shifts',__name__)
shifts_bl = ShiftBL()

#get ALL
@shifts.route("/", methods=['GET'])
def get_all_shifts():
    
    is_existing=request.args.get("is_existing")
    print(is_existing)
    shifts = action_verify_token(shifts_bl.get_all_shifts,[is_existing])
    return shifts


@shifts.route("/<id>",methods=['GET'])
def get_shift(id):
    shift_recv = action_verify_token(shifts_bl.get_shift,[id])
    return shift_recv


@shifts.route("/",methods=['POST'])
def add_shift():
    obj = request.json
    resp= action_verify_token(shifts_bl.add_shift,[obj])
    return resp


@shifts.route("/<id>",methods=['PUT'])
def update_shift(id):
    obj=request.json
    resp=action_verify_token(shifts_bl.update_shift,[id,obj])
    return resp


 