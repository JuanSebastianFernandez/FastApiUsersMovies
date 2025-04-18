from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from db.models.users_models import UserInDB, UserOut
from core.user_service import search_user
from core.security import hash_password

app = FastAPI()

#-------------------------------------------------- Dependencias --------------------------------------------------------------------
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: Annotated[str, Depends(oauth2)]) -> UserOut:
    user = decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid authentication credentials", 
            headers={"WWW-Authenticate": "Bearer"}
            )
    return user

#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_exist = search_user(id=None, email=form_data.username)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    if not user_exist[1].hashed_password == hash_password(form_data.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    return {"access_token": form_data.username, "token_type": "bearer"}



#--------------------------------------------------- Implementación mientras routeamos el main.py --------------------------------------------
@app.get("/users/me", response_model=UserOut, status_code=status.HTTP_200_OK)
async def read_user_me(current_user: Annotated[UserOut, Depends(get_current_user)]):
    return current_user


def decode_token(token: str):
    # Simulando la validación del token
    user_exist = search_user(id=None, email=token)
    return UserOut(**user_exist[1].model_dump())