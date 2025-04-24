from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status, Header
from jwt.exceptions import InvalidTokenError
from app.core.user_service import search_user
from app.db.models.movies_models import HeaderParams
from app.db.models.users_models import UserOut
from app.core.security import decode_acces_token
from sqlmodel import Session
from app.db.clientsql import get_session
from app.core.logger import logger
#-------------------------------------------------- Dependencias --------------------------------------------------------------------
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: Annotated[str, Depends(oauth2)], session: Annotated[Session, Depends(get_session)]) -> UserOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-authenticate": "Bearer"},
    )
    logger.info(f"Token {token}")
    try:

        decoded_token = decode_acces_token(token)
        logger.info(f"Get current user and decoded token bearer {decoded_token}")
        user_id = decoded_token.get("sub")
        if not user_id:
            raise credentials_exception
    except InvalidTokenError:
        logger.error(f"Get current user and decoded token bearer present error")
        raise credentials_exception
    
    user_exist = search_user(session=session, id=user_id)
    if not user_exist:
        raise credentials_exception
    return user_exist

def verify_token(x_token: Annotated[str | None, Header()] = None):
    if x_token != "secreto123":
        return False
    return True
        
def view_header_token(headers: Annotated[HeaderParams, Header()],
                        token: Annotated[bool, Depends(verify_token)]):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Token")
    return headers
