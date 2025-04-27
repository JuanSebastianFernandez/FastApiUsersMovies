from fastapi import APIRouter, Body, Path, Response, Cookie, status, Header, Depends, HTTPException
from typing import Annotated, Any
from uuid import UUID
from fastapi.responses import JSONResponse
from app.db.models.movies_models import Movie, HeaderParams
from app.db.data.movies_data import MOVIES_LIST as movies_list
from app.core.movies_service import search_movie
from app.dependencies import view_header_token
from app.db.moviesnosql import db_client
from app.core.logger import logger
from bson import ObjectId


router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)
# -------------------------------------------------- Definición de endpoints get ----------------------------------------------------

# Parametros de Header
@router.get("/", response_model=list[Movie], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
async def read_movies(headers: Annotated[Any, Depends(view_header_token)]) -> JSONResponse:
    
    movies_list = list(db_client.movies.find())
    if not movies_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No movies found")
    return JSONResponse(
        content={
            "message":"Movies found",
            "movies": [Movie(**movie, id=str(movie["_id"])).model_dump(mode="json", exclude_unset=True) for movie in movies_list]
        }
    )

# Get para establecer cookie
@router.get("/favorite/{movie_id}", response_model=None, status_code=status.HTTP_201_CREATED, dependencies=[Depends(view_header_token)])
async def set_favorite_movie(
    movie_id:Annotated[str,
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
    try:
        movie_exist = search_movie("_id", ObjectId(movie_id))
    except Exception as e:
        logger.error(f"Error searching movie: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message":"Internal Server Error, validate ID format"

                }
            )
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
    try:
        movie_exist = search_movie("_id", ObjectId(favorite_movie))
    except Exception as e:
        logger.error(f"Error searching movie: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message":"Internal Server Error, validate ID format"

                }
            )
    if not movie_exist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message":"Movie Not Found"
                }
            )
    return {"message":"Movie Founded",
            "movie":Movie(**movie_exist, id=str(movie_exist["_id"])).model_dump(mode="json", exclude_unset=True)}

# -------------------------------------------------- Definición de endpoints post ----------------------------------------------------
@router.post("/", response_model=Movie, response_model_exclude_unset=True, status_code=status.HTTP_201_CREATED)
async def create_movie(movie: Movie):
    movie_db = movie.model_dump(mode="json", exclude_unset=True)
    logger.info(f"Title: {movie_db["title"]}")
    founded_movie = search_movie("title", movie_db["title"])
    logger.info(f"Movie founded {founded_movie}")
    if founded_movie:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message":"Movie already exist",
                "movie": Movie(**founded_movie, id=str(founded_movie["_id"])).model_dump(mode="json", exclude_unset=True)

            }
        )
    del movie_db["id"]
    id = db_client.movies.insert_one(movie_db).inserted_id

    movie_inserted = db_client.movies.find_one({"_id":id})

    return Movie(**movie_inserted, id=str(id))
# -------------------------------------------------- Definición de endpoints put ----------------------------------------------------

@router.put("/{movie_id}", response_model=Movie, response_model_exclude_unset= True, status_code=status.HTTP_201_CREATED)
async def update_movie(
    movie_id:Annotated[str,
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
    try:
        movie_db = movie.model_dump(mode="json", exclude_unset=True)
        del movie_db["id"]
        updated_movie = db_client.movies.find_one_and_update(
            {"_id": ObjectId(movie_id)}, 
            {"$set": movie_db},
            return_document=True  # Para devolver el documento actualizado
        )
        if updated_movie:
            updated_movie["id"] = str(updated_movie["_id"])
            del updated_movie["_id"]
            return Movie(**updated_movie)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID")

# -------------------------------------------------- Definición de endpoints delete ----------------------------------------------------
@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(
    movie_id: Annotated[str, Path(
        title="El ID de la película a eliminar",
        description="El ID de la película a eliminar"
    )]
):
    try:
        deleted_movie = db_client.movies.find_one_and_delete({"_id": ObjectId(movie_id)})
        if deleted_movie:
            return  # <-- simplemente no retornas nada
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID")