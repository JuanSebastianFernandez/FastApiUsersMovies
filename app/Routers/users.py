import sys
import os

# Agregar el directorio padre (app) al sys.path sera eliminado cuando se llame como router en el main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, Query, Path, Body, Response, status
from typing import Annotated
from fastapi.responses import JSONResponse
from db.models.users_models import UserIn, UserOut, UserFilter
from db.data.users_data import USER_LIST as users_list

# Instanca de FasAPI
app = FastAPI()

#-------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de query
@app.get("/users/", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def read_users(filter_user: Annotated[UserFilter, Query()]):
    filtered_users = users_list[filter_user.start:filter_user.limit]
    if not filter_user.show_password:
        return filtered_users
    return JSONResponse(
        content=[user.model_dump() for user in filtered_users]
        ) 

# Parametros de ruta
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def read_user(
    user_id: Annotated[str, 
                        Path(
                            title="El ID del usuario a obtener",
                            description="El ID del usuario a obtener"
                            )]
    ) -> JSONResponse:
    user_exist = search_user(user_id)
    if not user_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": "User Not Found"
                }
            )
    return JSONResponse(
        content={
            "message":"User found",
            "user":UserOut(id=user_exist[1].id, 
                            name=user_exist[1].name, 
                            email=user_exist[1].email).model_dump()
                }
            )

#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@app.post("/users/", response_model=None, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn) -> JSONResponse:
    user_exist = search_user(user.id, user.email)
    if not user_exist:
        users_list.append(user)
        return JSONResponse(
            content = {
                "message":"User Created Successfully",
                "user": UserOut(id=user.id,
                                name=user.name,
                                email=user.email).model_dump()    
                }
            )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content = {
            "message":"User Already Exist", 
            "user":UserOut(id=user_exist[1].id, 
                            name=user_exist[1].name, 
                            email=user_exist[1].email).model_dump()
            }
        )

#-------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@app.put("/users/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_user(
    user_id: Annotated[str, 
                        Path(
                            title="El ID del usuario a obtener",
                            description="El ID del usuario a obtener",
                            )],
    user: Annotated[UserIn, 
                    Body(
                        embed=True
                        )]
    ) -> Response:

    user_exist = search_user(user_id)
    if not user_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message":"User Not Found"
                }
            )
    users_list[user_exist[0]] = user
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(id=user.id,
                            name=user.name,
                            email=user.email).model_dump()
            }
        )

#-------------------------------------------------- Definición de endpoints delete ----------------------------------------------------

@app.delete("/users/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def delete_user(user_id:str) -> JSONResponse:
    user_exist = search_user(user_id)
    if not user_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message":"User Not Found"
                }
            )
    user_deleted = users_list.pop(user_exist[0])
    return JSONResponse(
        content={
            "message":"User Deleted Successfully",
            "user_deleted":"True", 
            "user":UserOut(id=user_deleted.id, 
                            name=user_deleted.name, 
                            email=user_deleted.email).model_dump()
            }
        )
        
#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_user(id:str, email:str = None) -> tuple[int, UserIn]|None:
    for index, search_user in enumerate(users_list):
        if search_user.id == id or search_user.email == email:
            return index, search_user
    return None
        