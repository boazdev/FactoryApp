from datetime import datetime
from flask import Flask
import json
from bson import ObjectId
from flask_cors import CORS

from routers.auth_router import auth
from routers.user_router import users
from routers.employee_router import employees
from routers.department_router import departments
from routers.shift_router import shifts
from routers.actions_router import actions

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            #datetime.date.__str__
            return str(obj.date())
        return json.JSONEncoder.default(self,obj)

app = Flask(__name__)
app.url_map.strict_slashes = False
app.json_encoder = JSONEncoder
CORS(app)


app.register_blueprint(actions, url_prefix="/actions")
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(employees, url_prefix="/employees")
app.register_blueprint(departments, url_prefix="/departments")
app.register_blueprint(shifts, url_prefix="/shifts")

app.run()