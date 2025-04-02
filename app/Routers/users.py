from fastapi import FastAPI, Query, Path, Body, Response
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Annotated, Any
from fastapi.responses import JSONResponse


# Instanca de FasAPI
app = FastAPI()

# Definición de clase BasemModel User
class UserBase(BaseModel):
    id:int
    name:str
    email:EmailStr
class User(UserBase):
    password: str



# Definición de la clase de filtro de parametros
class UserFilter(BaseModel):
    start: Optional[int] = Field(
        default=0, 
        ge=0, 
        description="Índice de inicio para la paginación", 
        title="Indice inicio"
    )
    limit: Optional[int] = Field(
        default=None, 
        gt=0, 
        description="Cantidad máxima de usuarios a devolver", 
        title="Inidice Fin"
    )
    show_password: Optional[bool] = Field(
        default=False, 
        description="Indica si se debe mostrar el password de los usuarios", 
        title="Ver Password",
        deprecated=True
    )


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
async def read_users(filter_user: Annotated[UserFilter, Query()]):

    if not filter_user.show_password:
        new_list = [{"id": user.id, "name": user.name, 
                    "email": user.email} for user in users_list][filter_user.start:filter_user.limit]
        return new_list
    return users_list[filter_user.start:filter_user.limit]


# Parametros de ruta
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}", response_model=None)
async def read_user(
    user_id: Annotated[int, 
                        Path(
                            title="El ID del usuario a obtener",
                            gt=0,
                            le = len(users_list),
                            description="El ID del usuario a obtener"
                            )]
    ) -> Response | dict:
    user = search_user(user_id)
    if not user:
        return {"message": "User Not Found"}
    return JSONResponse(
        status_code=200,
        content={
            "message":"User found",
            "user":{
                "id":user[1].id,
                "name":user[1].name,
                "email":user[1].email
                    }
                }
            )

#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@app.post("/users/")
async def create_user(user: User) -> JSONResponse:
    user_exist = search_user(user.id, user.email)
    if not user_exist:
        users_list.append(user)
        return JSONResponse(
            status_code=201,
            content = {
                "message":"User Created Successfully",
                "user": {
                    "id":user.id,
                    "name":user.name,
                    "email":user.email
                }
            }

        )
    return JSONResponse(
        status_code=400,
        content = {
            "message":"User Already Exist", 
            "user": {
                "id":user_exist[1].id,
                "name":user_exist[1].name,
                "email":user_exist[1].email
                }
            }
        )


#-------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@app.put("/users/{user_id}")
async def update_user(
    user_id: Annotated[int, 
                        Path(
                            title="El ID del usuario a obtener",
                            gt=0,
                            le = len(users_list),
                            description="El ID del usuario a obtener",
                            )],
    user: Annotated[User, 
                    Body(
                        embed=True
                        )]
    ):

    user_exist = search_user(user_id)
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
        