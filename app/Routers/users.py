from fastapi import APIRouter, Query, Path, Body, Response, status, HTTPException, Depends
from typing import Annotated
from fastapi.responses import JSONResponse
from app.db.models.users_models import UserIn, UserOut, UserFilter
from app.db.data.users_data import USER_LIST as users_list
from app.core.user_service import search_user, save_user
from app.dependencies import get_current_user

# Instanca de FasAPI
router = APIRouter(
    prefix="/users", 
    tags=["Users"]
)

#-------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de query
@router.get("/", response_model=list[UserOut], 
            status_code=status.HTTP_200_OK, 
            tags=["Users"], 
            summary="Get all users", 
            response_description="Lista de usuarios",
            deprecated=False)
async def read_users(filter_user: Annotated[UserFilter, Query()]):
    """
    Obtener todos los usuarios de la base de datos.
    - **start**: Indice de inicio para la paginación.
    - **limit**: Cantidad máxima de usuarios a devolver.
    - **show_password**: Indica si se debe mostrar el password de los usuarios.
    """
    filtered_users = users_list[filter_user.start:filter_user.limit]
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
    user_id: Annotated[str, 
                        Path(
                            title="El ID del usuario a obtener",
                            description="El ID del usuario a obtener"
                            )]
    ) -> JSONResponse:
    user_exist = search_user(user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return JSONResponse(
        content={
            "message":"User found",
            "user":UserOut(**user_exist[1].model_dump()).model_dump()
                }
            )
    
#-------------------------------------------------- Definición de endpoints post ----------------------------------------------------

@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn) -> JSONResponse:
    user_exist = search_user(user.id, user.email)
    if not user_exist:
        users_list.append(save_user(user))
        return JSONResponse(
            content = {
                "message":"User Created Successfully",
                "user": UserOut(**user.model_dump()).model_dump()    
                }
            )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content = {
            "message":"User Already Exist", 
            "user":UserOut(**user.model_dump()).model_dump()
            }
        )

#-------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@router.put("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_user(
    user_id: Annotated[str, 
                        Path(
                            title="El ID del usuario a obtener",
                            description="El ID del usuario a obtener",
                            )],
    user: Annotated[UserIn, 
                    Body(
                        embed=True
                        )]
    ) -> Response:

    user_exist = search_user(user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    users_list[user_exist[0]] = save_user(user)
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(**user.model_dump()).model_dump()
            }
        )
    
#-------------------------------------------------- Definición de endpoints patch ----------------------------------------------------
@router.patch("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_item_user(
    user_id: str, 
    data: Annotated[dict, 
                    Body()]
    ) -> JSONResponse:

    user_exist = search_user(user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    # update_data = user.model_dump(exclude_unset=True)
    update_user = user_exist[1].copy(update=data)
    users_list[user_exist[0]] = update_user
    
    return JSONResponse(
        content={
            "message":"User Updated Successfully",
            "user": UserOut(**update_user.model_dump()).model_dump()
            }
        )
#-------------------------------------------------- Definición de endpoints delete ----------------------------------------------------

@router.delete("/{user_id}", response_model=None, status_code=status.HTTP_200_OK)
async def delete_user(user_id:str) -> JSONResponse:
    user_exist = search_user(user_id)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    user_deleted = users_list.pop(user_exist[0])
    return JSONResponse(
        content={
            "message":"User Deleted Successfully",
            "user_deleted":"True", 
            "user":UserOut(**user_deleted.model_dump()).model_dump()
            }
        )
        
