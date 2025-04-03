from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from uuid import UUID
from datetime import datetime

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

# Definición de un modelo para los parámetros de cabecera
class HeaderParams(BaseModel):
    user_agent: str|None
    x_token: str|None