from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Instanca de FasAPI
app = FastAPI()

# Definición de clase BasemModel User
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


# Base de datos simulada
users_list = [
    User(id=1, name="Juan Perez", email="juan_peres@gmail.com", password="123456"),
    User(id=2, name="Maria Lopez", email="maria_lopez@gmail.com", password="654312"),
    User(id=3, name="Carlos Perez", email="CarlosPerez@hotmail.com", password="5478621"),
    User(id=4, name="Ana Maria", email="Mana@hotmail.com", password="123456"),
    User(id=5, name="Jose Perez", email="Perezpereza@gmail.com", password="253698")
]

#-------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de query
@app.get("/users/")
def read_users(start: int = 0, limit: Optional[int] = None, show_email:bool = False):

    if not show_email:
        new_list = [{"id": user.id, "name": user.name, 
                    "password": user.password} for user in users_list][start:limit]
        return new_list
    return users_list[start:limit]

# Parametros de ruta
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):

    #search_user = next((user for user in users_list if user.id == user_id), None) una forma de hacerlo
    user = search_user(user_id)
    if not user:
        return {"message": "User Not Found"}
    return user[1]

#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@app.post("/users/")
async def create_user(user: User):

    user_exist = search_user(user.id, user.email)
    if not user_exist:
        users_list.append(user)
        return user
    return {"message":"User Already Exist", "user": users_list[user_exist[0]]}

#-------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@app.put("/users/")
async def update_user(user: User):

    user_exist = search_user(user.id)
    if not user_exist:
        return {"message":"User Not Found"}
    users_list[user_exist[0]] = user
    return user
    

#-------------------------------------------------- Definición de endpoints delete ----------------------------------------------------

@app.delete("/users/{user_id}")
async def delete_user(user_id:int):

    user_exist = search_user(user_id)
    if not user_exist:
        return {"message":"User Not Found"}
    user_deleted = users_list.pop(user_exist[0])
    return {"user_deleted":"True", "user":user_deleted}
        
#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_user(id:int, email:str = None):
    for index, search_user in enumerate(users_list):
        if search_user.id == id or search_user.email == email:
            return index, search_user
    return None
        