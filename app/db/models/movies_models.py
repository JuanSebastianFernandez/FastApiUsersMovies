from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from uuid import UUID
from datetime import datetime

class Imdb(BaseModel):
    rating: float
    votes: int
    id: int|None = None

class Awards(BaseModel):
    wins: int
    nominations: int
    text: str | None

class Viewer(BaseModel):
    rating: float | None = Field(
        default=None,
        examples=[
            7.2,  # rating
            8.8,  # rating
            9.0   # rating
        ]
    )
    numReviews: int | None = Field(
        default=None,
        examples=[
            1000,  # numReviews
            3500,  # numReviews
            5000   # numReviews
        ]
    )
    meter: int | None = Field(
        default=None,
        examples=[
            100,  # meter
            50,   # meter
            75    # meter
        ]
    )

class Critic(BaseModel):
    rating: float | None = Field(
        default=None,
        examples=[
            7.2,  # rating
            8.8,  # rating
            9.0   # rating
        ]
    )
    numReviews: int | None = Field(
        default=None,
        examples=[
            1000,  # numReviews
            3500,  # numReviews
            5000   # numReviews
        ]
    )
    meter: int | None = Field(
        default=None,
        examples=[
            100,  # meter
            50,   # meter
            75    # meter
        ]
    )
class Tomatoes(BaseModel):
    viewer: Optional[Viewer] = Field(
        default=None,
        examples=[
            {
                "rating": 7.2,
                "numReviews": 1000,
                "meter": 100
            },
            {
                "rating": 8.8,
                "numReviews": 3500,
                "meter": 50
            }
        ]
    )
    fresh: int | None = Field(
        default=None,
        examples=[
            100,  # fresh
            50,   # fresh
            25    # fresh
        ]
    )
    critic: Optional[Critic] = Field(
        default=None,
        examples=[
            {
                "rating": 7.2,
                "numReviews": 1000,
                "meter": 100
            },
            {
                "rating": 8.8,
                "numReviews": 3500,
                "meter": 50
            }
        ]
    )
    rotten: int | None = Field(
        default=None,
        examples=[
            100,  # rotten
            50,   # rotten
            25    # rotten
        ]
    )

    dvd: Optional[datetime] = Field(
        default=None,
        examples=[
            "2023-10-01T00:00:00Z",
            "2022-05-15T00:00:00Z"
        ]
    )
    lastUpdated: Optional[datetime] = Field(
        default=None,
        examples=[
            "2023-10-01T00:00:00Z",
            "2022-05-15T00:00:00Z"
        ]
    )


class Movie(BaseModel):
    id : str|None= Field(
        examples=["12345678-1234-5678-1234-567812345678"]
    )
    plot: str | None = Field(
        default=None,
        examples=["This is a movie about........."]
    )
    genres: list[str] = Field(
        default=["Animation", "Comedy"],
        examples=[
            ["Animation", "Comedy"],
            ["Drama"],
            ["Drama", "Romance"]
        ]
    )
    runtime: int | None = Field(
        default = None,
        examples=[
            12,  # minutos
            90,  # minutos
            120  # minutos
        ]
    )
    cast: list[str] = Field(
        default=["Gertie", "Winsor McCay"],
        examples=[
            ["Gertie", "Winsor McCay"],
            ["Al Jolson"],
            ["Charles Bryant", "Alla Nazimova"]
        ]
    )
    num_mflix_comments: int | None = Field(
        default=None,
        examples=[
            0,  # comentarios
            1,  # comentarios
            2   # comentarios
        ]
    )
    poster: HttpUrl | None = Field(
        default=None,
        examples=[
            "https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg",
            "https://m.media-amazon.com/images/M/MV5BZGEwNTA3MjgtYzE0Mi00MjQ2LThkNjAtYzcyODE3NDBjODIwXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SY1000_SX677_AL_.jpg"
        ]
    )
    title: str = Field(
        examples=["Gertie the Dinosaur", "The Jazz Singer", "Salomé"]
    )
    fullplot: str | None = Field(
        default=None,
        examples=[
            "The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
            "The first feature-length film with synchronized sound.",
            "A silent film adaptation of Oscar Wilde's play."
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
    released: Optional[datetime] = Field(
        default=None,
        examples=[
            "2023-10-01T00:00:00Z",
            "2022-05-15T00:00:00Z"
        ]
    )
    directors: list[str] = Field(
        examples=[
            ["Winsor McCay", "others..."],
            ["Alan Crosland"],
            ["Charles Bryant", "Alla Nazimova"]
        ]
    )
    rated:  str | None = Field(
        default=None,
        examples=[
            "G",  # General
            "PG", # Parental Guidance
            "PG-13", # Parents Strongly Cautioned
            "R"   # Restricted
        ]
    )
    writers: list[str] = Field(
        default=["Winsor McCay", "others..."],
        examples=[
            ["Winsor McCay", "others..."],
            ["Al Jolson"],
            ["Charles Bryant", "Alla Nazimova"]
        ]
    )
    awards: Optional[Awards] = Field(
        default=None,
        examples=[
            {"wins": 1, "nominations": 0, "text": "Won 1 Oscar."},
            {"wins": 0, "nominations": 0, "text": "No awards."},
            {"wins": 2, "nominations": 1, "text": "Won 2 Oscars."}]
    )
    lastupdated: Optional[datetime] = Field(
        default=None,
        examples=[
            "2023-10-01T00:00:00Z",
            "2022-05-15T00:00:00Z"
        ]
    )
    year : int = Field(
        examples=[1914, 1927, 1922],
        gt=1888,    # Primer año de cine
        le=2025    # Año actual
    )
    imdb: Optional[Imdb] = Field(
        default=None,
        examples=[
            {"rating": 7.2, "votes": 1000},
            {"rating": 8.8, "votes": 3500}
        ]
    )
    countries:list[str] = Field(
        default=["USA"],
        examples=[
            ["USA"],
            ["USA", "UK"],
            ["USA", "UK", "France"]
        ]
    )
    type: str = Field(
        default="movie",
        examples=[
            "movie",
            "series",
            "short"
        ]
    )
    tomatoes: Optional[Tomatoes] = Field(
        default=None,
        examples=[
            {
                "viewer": {
                    "rating": 7.2,
                    "numReviews": 1000,
                    "meter": 100
                },
                "dvd": "2023-10-01T00:00:00Z",
                "lastUpdated": "2023-10-01T00:00:00Z"
            },
            {
                "viewer": {
                    "rating": 8.8,
                    "numReviews": 3500,
                    "meter": 50
                },
                "dvd": "2022-05-15T00:00:00Z",
                "lastUpdated": "2022-05-15T00:00:00Z"
            }
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

# Definición de un modelo para los parámetros de cabecera
class HeaderParams(BaseModel):
    user_agent: str|None
    x_token: str|None