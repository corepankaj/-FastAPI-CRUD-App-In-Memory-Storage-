from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Temporary in-memory storage
todos = []

class User(BaseModel):
    id: int
    name: str
    city: str
    age: int

# Create user
@app.post("/todo")
def create_user(user: User):
    todos.append(user)
    return {"message": "User added", "user": user}

# Get all users
@app.get("/todo")
def get_users():
    return todos

# Get single user
@app.get("/todo/{u_id}")
def get_user(u_id: int):
    for user in todos:
        if user.id == u_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Update user
@app.put("/todo/{u_id}")
def update_user(u_id: int, updated_user: User):
    for index, user in enumerate(todos):
        if user.id == u_id:
            todos[index] = updated_user
            return {"message": "User updated", "user": updated_user}
    raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/todo/{u_id}")
def delete_user(u_id: int):
    for index, user in enumerate(todos):
        if user.id == u_id:
            deleted_user = todos.pop(index)
            return {"message": "User deleted", "user": deleted_user}
    raise HTTPException(status_code=404, detail="User not found")