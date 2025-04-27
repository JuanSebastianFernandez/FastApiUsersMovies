from uuid import UUID
from app.db.data.movies_data import MOVIES_LIST as movies_list
from app.db.models.movies_models import Movie
from app.db.moviesnosql import db_client
from app.core.logger import logger
#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_movie(field:str, key):
    try:
        logger.info(f"Search movie by {field}:{key}")
        movie = db_client.local.movies.find_one({field: key})
        logger.info(f"Movie found {movie}")
        return movie
    except:
        return None