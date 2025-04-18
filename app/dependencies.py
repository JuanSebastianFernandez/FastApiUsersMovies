from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.db.models.users_models import UserOut
from fastapi import Depends, HTTPException, status
from app.core.security import decode_acces_token
from jwt.exceptions import InvalidTokenError
from app.core.user_service import search_user

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