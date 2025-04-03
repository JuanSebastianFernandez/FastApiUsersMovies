from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Definición de clase BasemModel User
class UserIn(BaseModel):
    id:str
    name:str
    email:EmailStr
    password: str

class UserOut(BaseModel):
    id:str
    name:str
    email:EmailStr

class UserInDB(BaseModel):
    id:str
    name:str
    email:EmailStr
    hashed_password: str

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