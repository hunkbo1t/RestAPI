#pip install fastAPI
#pip install uvicorn
#pip install Jinja2
#start server :> uvicorn file_name:app      eg.uvicorn main:app

from os import name
from typing import Optional
from fastapi import FastAPI
from fastapi import templating
from fastapi import responses
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

template = Jinja2Templates("static")

class AssignmentData(BaseModel):
    user_name: str
    assignment_number: int
    desc: str

@app.get("/",response_class=HTMLResponse)
def base_home(request: Request):
    print('return HTML')
    return template.TemplateResponse('index.html',{"request":request})

@app.get("/home/{user}")
def home(user: str):
    return {
        "user-name": user
    }
#          /home/queries/dev?query=FAQs
@app.get("/home/queries/{user}")
def handling_queries(user: str,query: Optional[str]):
    return{
        "user": user,
        "query": query
    }

@app.post("/home/assignment")
def submit_assignment(assignment_data: AssignmentData):
    print(assignment_data.user_name,assignment_data.assignment_number,assignment_data.desc)
    return{
        "user": assignment_data.user_name,
        "number": assignment_data.assignment_number,
        "description": assignment_data.desc,
        "submit": "Success"
    }