from fastapi import FastAPI
from pydantic import BaseModel 

class Users(BaseModel):
    name:str
    age:int
    skill:str
    
app = FastAPI()

@app.post("/create")
def create_usr(user:Users):
    return{"message":"data has been created", "data":user}