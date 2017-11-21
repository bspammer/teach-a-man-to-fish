from flask import Flask
import todoist as tdi

app = Flask(__name__)
api = tdi.TodoistAPI()
with open("private/apitoken") as f:
    api.token = f.read().strip()
api.sync()
with open("private/shoppingprojectid") as f:
    shopping_project_id = f.read().strip()

import teachamantofish.views
