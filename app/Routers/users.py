import sys
import os

# Agregar el directorio padre (app) al sys.path sera eliminado cuando se llame como router en el main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, Query, Path, Body, Response, status, Form, HTTPException, Depends
from typing import Annotated
from fastapi.responses import JSONResponse
from db.models.users_models import UserIn, UserOut, UserFilter, UserInDB, FormData
from db.data.users_data import USER_LIST as users_list
from db.data.users_data import hash_password
# Instanca de FasAPI
app = FastAPI()

#-------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de query
@app.get("/users/", response_model=list[UserOut], 
            status_code=status.HTTP_200_OK, 
            tags=["Users"], 
            summary="Get all users", 
            response_description="Lista de usuarios",
            deprecated=False)
async def read_users(filter_user: Annotated[UserFilter, Query()]):
    """
    Obtener todos los usuarios de la base de datos.
    - **start**: Indice de inicio para la paginación.
    - **limit**: Cantidad máxima de usuarios a devolver.
    - **show_password**: Indica si se debe mostrar el password de los usuarios.
    """
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return JSONResponse(
        content={
            "message":"User found",
            "user":UserOut(**user_exist[1].model_dump()).model_dump()
                }
            )
    
#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@app.post("/users/", response_model=None, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn) -> JSONResponse:
    user_exist = search_user(user.id, user.email)
    if not user_exist:
        users_list.append(save_user(user))
        return JSONResponse(
            content = {
                "message":"User Created Successfully",
                "user": UserOut(**user.model_dump()).model_dump()    
                }
            )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content = {
            "message":"User Already Exist", 
            "user":UserOut(**user.model_dump()).model_dump()
            }
        )
    
@app.post("/users/login/", response_model=None, status_code=status.HTTP_200_OK)
async def login_user(data: Annotated[FormData, Form()]):
    user_exist = search_user(id = None, email = data.email)
    print(user_exist)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    if user_exist[1].hashed_password == hash_password(data.password):
        return JSONResponse(
            content={
                "message":"Login Successfully",
                "user":UserOut(**user_exist[1].model_dump()).model_dump()
                }
            )
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Password Incorrect")

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    users_list[user_exist[0]] = save_user(user)
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(**user.model_dump()).model_dump()
            }
        )
    
#-------------------------------------------------- Definición de endpoints patch ----------------------------------------------------
@app.patch("/users/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_item_user(
    user_id: str, 
    data: Annotated[dict, 
                    Body()]
    ) -> JSONResponse:

    user_exist = search_user(user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    # update_data = user.model_dump(exclude_unset=True)
    update_user = user_exist[1].copy(update=data)
    users_list[user_exist[0]] = update_user
    
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(**update_user.model_dump()).model_dump()
            }
        )
#-------------------------------------------------- Definición de endpoints delete ----------------------------------------------------

@app.delete("/users/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def delete_user(user_id:str) -> JSONResponse:
    user_exist = search_user(user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    user_deleted = users_list.pop(user_exist[0])
    return JSONResponse(
        content={
            "message":"User Deleted Successfully",
            "user_deleted":"True", 
            "user":UserOut(**user_deleted.model_dump()).model_dump()
            }
        )
        
#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_user(id:str, email:str = None) -> tuple[int, UserInDB]|None:
    for index, search_user in enumerate(users_list):
        if search_user.id == id or search_user.email == email:
            return index, search_user
    return None

def save_user(user_in:UserIn):
    hashed_password = hash_password(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    
    return user_in_db