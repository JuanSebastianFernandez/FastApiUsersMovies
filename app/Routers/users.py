from fastapi import APIRouter, Query, Path, Body, Response, status, HTTPException, Depends, BackgroundTasks
from typing import Annotated
from fastapi.responses import JSONResponse
from sqlmodel import select
from app.db.models.users_models import UserIn, UserOut, UserFilter, UserInDB, UserUpdate
from app.core.user_service import search_user, save_user, write_notification
from app.dependencies import get_current_user
from app.db.clientsql import create_db_and_tables, sessionDep
from app.core.logger import logger


logger.info("Cargando el router de users")
# Instanca de FasAPI
router = APIRouter(
    prefix="/users", 
    tags=["Users"]
)

#-------------------------------------------------- Definición de eventos ----------------------------------------------------
@router.on_event("startup")
def on_startup():
    """
    Crear las tabas al iniciar la sesión.
    """
    create_db_and_tables()
    

#-------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de query
@router.get("/", response_model=list[UserOut], 
            status_code=status.HTTP_200_OK, 
            tags=["Users"], 
            summary="Get all users", 
            response_description="Lista de usuarios")
async def read_users(session: sessionDep, filter_user: Annotated[UserFilter, Query()]):
    """
    Obtener todos los usuarios de la base de datos.
    - **start**: Indice de inicio para la paginación.
    - **limit**: Cantidad máxima de usuarios a devolver.
    - **show_password**: Indica si se debe mostrar el password de los usuarios.
    """
    filtered_users = session.exec(select(UserInDB).offset(filter_user.start).limit(filter_user.limit)).all()
    
    if not filter_user.show_password:
        return filtered_users
    return JSONResponse(
        content=[user.model_dump() for user in filtered_users]
        )


@router.get("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
async def read_user_me(current_user: Annotated[UserOut, Depends(get_current_user)]):
    return current_user



@router.get("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def read_user(
    user_id: Annotated[int, 
                        Path(
                            title="El ID del usuario a obtener",
                            description="El ID del usuario a obtener"
                            )],
    session:sessionDep
    ) -> JSONResponse:

    user_exist = search_user(session, user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return JSONResponse(
        content={
            "message":"User found",
            "user":UserOut(**user_exist.model_dump()).model_dump()
                }
            )
    
#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------


@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn, session: sessionDep) -> JSONResponse:
    user_exist = search_user(session, None, user.email)
    if not user_exist:
        db_user = save_user(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return JSONResponse(
                content = {
                    "message":"User Created Successfully",
                    "user": user.model_dump()  
                    }
                )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content = {
            "message":"User Already Exist", 
            "user":UserOut(**user_exist.model_dump()).model_dump()
            }
        )


@router.post("/notification/{email}", response_model=None, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)])
async def create_notification(email: str, backgroundtask: BackgroundTasks) -> JSONResponse:
    """
    Enviar una notificación al usuario por correo electrónico.
    - **email**: Correo electrónico del usuario.
    """
    backgroundtask.add_task(write_notification, email=email, message="Notification sent")
    return JSONResponse(
        content={
            "message":"Notification sent",
            "email":email
            }
        )
#-------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@router.put("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_user(
    user_id: Annotated[int, 
                        Path(
                            title="El ID del usuario a obtener",
                            description="El ID del usuario a obtener",
                            )],
    user: Annotated[UserIn, 
                    Body(
                        embed=True
                        )],
    session:sessionDep
    ) -> Response:

    user_exist = search_user(session, user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    user_exist.sqlmodel_update(user.model_dump())
    session.add(user_exist)
    session.commit()
    session.refresh(user_exist)
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(**user_exist.model_dump()).model_dump()
            }
        )
    
#-------------------------------------------------- Definición de endpoints patch ----------------------------------------------------
@router.patch("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_item_user(
    user_id: int, 
    user: Annotated[UserUpdate, 
                    Body()],
    session: sessionDep
    ) -> JSONResponse:

    user_exist = search_user(session, user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    user_exist.sqlmodel_update(user.model_dump(exclude_unset=True))
    session.add(user_exist)
    session.commit()
    session.refresh(user_exist)
    
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(**user_exist.model_dump()).model_dump()
            }
        )
#-------------------------------------------------- Definición de endpoints delete ----------------------------------------------------

@router.delete("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def delete_user(user_id:str, session: sessionDep) -> JSONResponse:
    user_exist = search_user(session, user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    session.delete(user_exist)
    session.commit()
    return JSONResponse(
        content={
            "message":"User Deleted Successfully",
            "user_deleted":"True", 
            "user":UserOut(**user_exist.model_dump()).model_dump()
            }
        )
        
