import sys
import os

# Agregar el directorio padre (app) al sys.path sera eliminado cuando se llame como router en el main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.models.users_models import UserIn, UserInDB
from db.data.users_data import USER_LIST as users_list
from db.data.users_data import hash_password
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