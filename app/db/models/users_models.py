from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from sqlmodel import Field as FieldSQL, SQLModel

# Definición de clase BasemModel User
# class UserBase(BaseModel):
#     id : str
#     name: str
#     email: EmailStr
class UserBase(SQLModel):  # Modelo base no tabla para la base de datos
    name: str = FieldSQL(max_length=50, title="Nombre del usuario", index=True)
    email: EmailStr = FieldSQL(max_length=50, title="Email del usuario", index=True, unique=True)

# class UserIn(UserBase):
#     password: str
class UserInDB(UserBase, table=True): # MOdelo que si es tabla para la base de datos
    id:int|None = FieldSQL(default=None, primary_key=True, title="ID del usuario")
    password: str = FieldSQL(max_length=150, title="Password del usuario", min_length=8)
    
class UserOut(UserBase):
    id: int

# class UserInDB(UserBase):
#     hashed_password: str

class UserIn(UserBase):
    password: str

class UserUpdate(UserBase):
    name:str|None = None
    email:str|None = None
    password:str|None = None

class FormData(BaseModel):
    email: str
    password: str
    model_config = {"extra": "forbid"}
    
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