from uuid import UUID
from app.db.data.movies_data import MOVIES_LIST as movies_list
from app.db.models.movies_models import Movie

#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_movie(id:UUID) -> tuple[int, Movie]|None:
    for index, movie in enumerate(movies_list):
        if movie.id == id:
            return index, movie
    return None