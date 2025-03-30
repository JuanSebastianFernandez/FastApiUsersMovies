from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, HttpUrl
from typing import Optional, Annotated

app = FastAPI()

# Definición de un submodelo
class Imdb(BaseModel):
    rating: float
    votes: int

class Movie(BaseModel):
    id: int
    title: str
    plot: str | None = None
    year : int
    directors: list[str]
    languages: set[str] = set()
    imdb: Optional[Imdb] = None
    poster: HttpUrl | None = None


# Base de datos simulada
movies_list = [
    Movie(
        id=1, 
        title="Gertie the Dinosaur", 
        plot="The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
        year=1914, 
        directors=["Winsor McCay"],
        languages={"English", "Spanish"},
        imdb = {
            "rating": 7.2,
            "votes": 1000
        },
        poster="https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg"
        ),
    Movie(
        id=2, 
        title="The Jazz Singer",
        plot = "The first feature-length motion picture with synchronized dialogue sequences.",
        year=1927, 
        directors=["Alan Crosland"],
        languages={"English", "Spanish"},
        imdb=Imdb(rating=7.0, votes=2000),
        poster="https://m.media-amazon.com/images/M/MV5BZGEwNTA3MjgtYzE0Mi00MjQ2LThkNjAtYzcyODE3NDBjODIwXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SY1000_SX677_AL_.jpg"
        ),
    Movie(
        id=3, 
        title="Salomé",
        plot="Salome, the daughter of Herodias, seduces her step-father/uncle Herod, governor of Judea, with a salacious dance. In return, he promises her the head of the prophet John the Baptist.", 
        year=1922, 
        directors=["Charles Bryant", "Alla Nazimova"],
        imdb=Imdb(rating=8.8, votes=3500),
        poster="https://m.media-amazon.com/images/M/MV5BMjA0MTY4MzI2OV5BMl5BanBnXkFtZTgwNTMyODg5MTE@._V1_SY1000_SX677_AL_.jpg"
        ),
    Movie(
        id=4, 
        title="Wings", 
        year=1927, 
        directors=["William A. Wellman", "Harry d'Abbadie d'Arrast"],
        languages={"English", "Spanish", "French"},
        imdb=Imdb(rating=6.4, votes=2000),
        poster = "https://m.media-amazon.com/images/M/MV5BYTI1YjgzZmMtZmIyYy00YTkwLTgyOWEtOTVlNTFkZmMzNTk3XkEyXkFqcGdeQXVyMDI2NDg0NQ@@._V1_SY1000_SX677_AL_.jpg"
        ),
    Movie(
        id=5, 
        title="The Phantom of the Opera", 
        year=1925, 
        directors=["Rupert Julian"],
        imdb=Imdb(rating=7.3, votes=4500),
        poster = "https://m.media-amazon.com/images/M/MV5BMmUzMDFiMjItMDdmMS00MmVlLWEyODAtOTRhODZjZjEyYmM2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX677_AL_.jpg"
        ),
    Movie(
        id=6, 
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
    movie_id:Annotated[int,
                        Path(
                            title="El ID de la película a obtener",
                            description="El ID de la película a obtener",
                            gt=0,
                            le=len(movies_list)
                        )],
    movie:Annotated[Movie, 
                    Body(
                        embed=True,
                        title="Actualizar película",
                        description="Actualizar película"
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