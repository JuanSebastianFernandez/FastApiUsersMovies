from fastapi import APIRouter, Body, Path, Response, Cookie, status, Header, Depends, HTTPException
from typing import Annotated, Any
from uuid import UUID
from fastapi.responses import JSONResponse
from app.db.models.movies_models import Movie, HeaderParams
from app.db.data.movies_data import MOVIES_LIST as movies_list
from app.core.movies_service import search_movie
from app.dependencies import view_header_token


router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)
# -------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de Header
@router.get("/", response_model=None, response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
async def read_movies(headers: Annotated[Any, Depends(view_header_token)]) -> JSONResponse:
    
    return JSONResponse(
        content={
            "message":"Token Correct",
            "user_agent": headers.user_agent,
            "Movies":[movie.model_dump(mode="json", exclude_unset=True) for movie in movies_list]
            }
        )

# Get para establecer cookie
@router.get("/favorite/{movie_id}", response_model=None, status_code=status.HTTP_201_CREATED, dependencies=[Depends(view_header_token)])
async def set_favorite_movie(
    movie_id:Annotated[UUID,
                        Path(
                            title="El ID de la película con like",
                            description="El ID de la película con like"
                            )
                        ]
    ) -> Response:
    response = JSONResponse(
        content={
            "message":f"Movie {movie_id} set as favorite"
            }
        )
    movie_exist = search_movie(movie_id)
    if not movie_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message":"Movie Not Found"
                }
            )
    response.set_cookie(key="favorite_movie", value=str(movie_id), expires=60)
    return response

# Parametros de cookie  
@router.get("/favorite", response_model=None, status_code=status.HTTP_200_OK, response_model_exclude_unset=True)
async def get_favorite_movie(favorite_movie:Annotated[str|None, 
                                                    Cookie(
                                                        title="ID de la película favorita"
                                                    )
                                                    ] = None
    ) -> Response | dict:
    if not favorite_movie:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message":"No favorite movie set"
                }
            )
    movie_exist = search_movie(UUID(favorite_movie))
    if not movie_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message":"Movie Not Found"
                }
            )
    return {"message":"Movie Founded",
            "movie":movie_exist[1]}

# -------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@router.put("/{movie_id}", response_model=Movie, response_model_exclude_unset= True, status_code=status.HTTP_201_CREATED)
async def update_movie(
    movie_id:Annotated[UUID,
                        Path(
                            title="El ID de la película a obtener",
                            description="El ID de la película a obtener"
                        )],
    movie:Annotated[Movie, 
                    Body(
                        embed=True,
                        title="Actualizar película",
                        description="Actualizar película",
                        examples=[
                                    {
                                        "id": "12345678-1234-5678-1234-567812345678", 
                                        "title": "Gertie the Dinosaur",
                                        "plot": "The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
                                        "year": 1914,
                                        "directors": ["Winsor McCay", "others..."],
                                        "languages": ["English", "Spanish"],
                                        "imdb": {
                                            "rating": 7.2,
                                            "votes": 1000
                                            },
                                        "poster":"https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg"
                                        
                                    },
                                    {
                                        "id": "12345678-1234-5678-1234-567812345678", 
                                        "title": "Gertie the Dinosaur",
                                        "year": 1914,
                                        "directors": ["Winsor McCay", "others..."]
                                        
                                    },
                                {
                                        "id": 1,
                                        "title": "Gertie the Dinosaur",
                                        "year": 1914,
                                        "directors": []
                                        
                                    }
                                
                            ]
                        )
                    ]
    ) -> JSONResponse:
    movie_exist = search_movie(movie_id)
    if not movie_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message":"Movie Not Found"
                }
            )
    movies_list[movie_exist[0]] = movie
    return movie
