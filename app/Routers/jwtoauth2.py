import sys
import os

# Agregar el directorio padre (app) al sys.path sera eliminado cuando se llame como router en el main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from db.models.users_models import UserInDB, UserOut
from db.models.security_models import Token
from core.user_service import search_user
from core.security import verify_password, create_acces_token, decode_acces_token
from datetime import timedelta
from jwt.exceptions import InvalidTokenError

app = FastAPI()

ACCES_TOKEN_EXPIRE_MINUTES = 1


#-------------------------------------------------- Dependencias --------------------------------------------------------------------
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: Annotated[str, Depends(oauth2)]) -> UserOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decoded_token = decode_acces_token(token)
        user_id = decoded_token.get("sub")
        if not user_id:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    
    user_exist = search_user(id=user_id)
    if not user_exist:
        raise credentials_exception
    return user_exist[1]

#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_exist = search_user(id=None, email=form_data.username)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    if not verify_password(form_data.password, user_exist[1].hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    
    acces_token_expires = timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    acces_token = create_acces_token(
        data={
            "sub":user_exist[1].id, 
            "email":user_exist[1].email
            }, 
        expires_delta=acces_token_expires
        )
    return Token(access_token=acces_token, token_type="bearer")



#--------------------------------------------------- Implementación mientras routeamos el main.py --------------------------------------------
@app.get("/users/me", response_model=UserOut, status_code=status.HTTP_200_OK)
async def read_user_me(current_user: Annotated[UserOut, Depends(get_current_user)]):
    return current_user
