from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.db.models.users_models import UserOut
from app.db.models.security_models import Token
from app.core.user_service import search_user
from app.core.security import verify_password, create_acces_token
from datetime import timedelta
from app.db.clientsql import create_db_and_tables, sessionDep

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

ACCES_TOKEN_EXPIRE_MINUTES = 3


#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session:sessionDep):
    user_exist = search_user(session=session, id=None, email=form_data.username)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    if not verify_password(form_data.password, user_exist.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    
    acces_token_expires = timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    acces_token = create_acces_token(
        data={
            "sub":str(user_exist.id),
            "email":user_exist.email
            }, 
        expires_delta=acces_token_expires
        )
    return Token(access_token=acces_token, token_type="bearer")