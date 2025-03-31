from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Annotated
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI()

# Definición de un submodelo
class Imdb(BaseModel):
    rating: float
    votes: int

class Movie(BaseModel):
    id : UUID = Field(
        examples=[UUID("12345678-1234-5678-1234-567812345678")]
    )
    title: str = Field(
        examples=["Gertie the Dinosaur", "The Jazz Singer", "Salomé"]
    )
    plot: str | None = Field(
        default=None,
        examples=["This is a movie about........."]
    )
    year : int = Field(
        examples=[1914, 1927, 1922],
        gt=1888,    # Primer año de cine
        le=2025    # Año actual
    )
    directors: list[str] = Field(
        examples=[
            ["Winsor McCay", "others..."],
            ["Alan Crosland"],
            ["Charles Bryant", "Alla Nazimova"]
        ]
    )
    languages: set[str] = Field(
        default=set(),
        examples=[
            {"English", "Spanish"},
            {"English", "Spanish", "French"},
            {"English", "Spanish", "French", "German"}
        ]
    )
    imdb: Optional[Imdb] = Field(
        default=None,
        examples=[
            {"rating": 7.2, "votes": 1000},
            {"rating": 8.8, "votes": 3500}
        ]
    )
    poster: HttpUrl | None = Field(
        default=None,
        examples=[
            "https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg",
            "https://m.media-amazon.com/images/M/MV5BZGEwNTA3MjgtYzE0Mi00MjQ2LThkNjAtYzcyODE3NDBjODIwXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SY1000_SX677_AL_.jpg"
        ]
    )
    released: Optional[datetime] = Field(
        default=None,
        examples=[
            "2023-10-01T00:00:00Z",
            "2022-05-15T00:00:00Z"
        ]
    )
    model_config = {
        "json_schema_extra":{
            "examples": [
                {
                    "id":"12345678-1234-5678-1234-567812345678", 
                    "title":"Gertie the Dinosaur",
                    "plot":"The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
                    "year":1914,
                    "directors":["Winsor McCay", "others..."],
                    "languages": ["English", "Spanish"],
                    "imdb": {
                        "rating": 7.2,
                        "votes": 1000
                    },
                    "poster":"https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg"
                }
            ]
        }
    }


# Base de datos simulada
movies_list = [
    Movie(
        id="9e08ee7a-dcfe-445d-958c-b01e7c51baa4", 
        title="Gertie the Dinosaur", 
        plot="The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
        year=1914, 
        directors=["Winsor McCay"],
        languages={"English", "Spanish"},
        imdb = {
            "rating": 7.2,
            "votes": 1000
        },
        poster="https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1914,9,15)
        ),
    Movie(
        id="ec61e0a8-0bf2-40da-8dd9-d3c72a9d207e", 
        title="The Jazz Singer",
        plot = "The first feature-length motion picture with synchronized dialogue sequences.",
        year=1980, 
        directors=["Alan Crosland"],
        languages={"English", "Spanish"},
        imdb=Imdb(rating=7.0, votes=2000),
        poster="https://m.media-amazon.com/images/M/MV5BZGEwNTA3MjgtYzE0Mi00MjQ2LThkNjAtYzcyODE3NDBjODIwXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1980,12,19)
        ),
    Movie(
        id="7b6777a0-ff22-43c3-98a1-a58eff31d90b", 
        title="Salomé",
        plot="Salome, the daughter of Herodias, seduces her step-father/uncle Herod, governor of Judea, with a salacious dance. In return, he promises her the head of the prophet John the Baptist.", 
        year=1922, 
        directors=["Charles Bryant", "Alla Nazimova"],
        imdb=Imdb(rating=8.8, votes=3500),
        poster="https://m.media-amazon.com/images/M/MV5BMjA0MTY4MzI2OV5BMl5BanBnXkFtZTgwNTMyODg5MTE@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1923,2,15)
        ),
    Movie(
        id="3cdbb4a7-500e-4adb-9996-4cc2324a138c", 
        title="Wings", 
        year=1929, 
        directors=["William A. Wellman", "Harry d'Abbadie d'Arrast"],
        languages={"English", "Spanish", "French"},
        imdb=Imdb(rating=6.4, votes=2000),
        poster = "https://m.media-amazon.com/images/M/MV5BYTI1YjgzZmMtZmIyYy00YTkwLTgyOWEtOTVlNTFkZmMzNTk3XkEyXkFqcGdeQXVyMDI2NDg0NQ@@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1929,1,5)
        ),
    Movie(
        id="ebcc5802-8efb-49f3-aa5c-58e007db5761", 
        title="The Phantom of the Opera", 
        year=1989, 
        directors=["Rupert Julian"],
        imdb=Imdb(rating=7.3, votes=4500),
        poster = "https://m.media-amazon.com/images/M/MV5BMmUzMDFiMjItMDdmMS00MmVlLWEyODAtOTRhODZjZjEyYmM2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1989,11,4)
        ),
    Movie(
        id="dd7262d0-a447-409c-8389-41c89db6a308", 
        title="The Gold Rush",
        plot="A lone prospector ventures into Alaska looking for gold and finds it and more.", 
        year=1925, 
        directors=["Charlie Chaplin"],
        languages={"English", "Spanish", "French", "German"},
        imdb=Imdb(rating=8.2, votes=5000)
        )
]


@app.get("/movies/")
async def read_movies():
    return movies_list

@app.put("/movies/{movie_id}")
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
    ):
    movie_exist = search_movie(movie_id)
    if not movie_exist:
        return {"message":"Movie Not Found"}
    movies_list[movie_exist[0]] = movie
    return movie

def search_movie(id:int):
    for index, movie in enumerate(movies_list):
        if movie.id == id:
            return index, movie
    return None