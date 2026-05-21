from fastapi import FastAPI
app = FastAPI()



@app.get("/")
def home():
    return {"message":"Welcome to Home page"}

@app.get("/users")
def user_info():
    return {"dsfdsf":"dfdsf"}

#path parameter
@app.get("/users/{user_id}")
def show_user(user_id:int):
    return {"userid": user_id}

#Query parameter
@app.get("/users1")
def get_user(name:str=None,age:int=40):
    return {"name":name,"age":age,"city":"Noida"}

#post data
@app.post("/create")
def create_useser(name:str, age:int):
    return {
          "name":name,
          "age":age
    }
#post data
@app.post("/create1")
def create_user1(user:dict):
    return{"message":"user has been created", "data":user}
