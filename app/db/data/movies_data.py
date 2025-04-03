from datetime import datetime
import sys
import os

# Agregar el directorio padre (db) al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.movies_models import Movie, Imdb
from uuid import uuid4

# Base de datos simulada
MOVIES_LIST = [
    # Tus 6 películas originales
    Movie(
        id="9e08ee7a-dcfe-445d-958c-b01e7c51baa4", 
        title="Gertie the Dinosaur", 
        plot="The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
        year=1914, 
        directors=["Winsor McCay"],
        languages={"English", "Spanish"},
        imdb=Imdb(rating=7.2, votes=1000),
        poster="https://m.media-amazon.com/images/M/MV5BMTQxNzI4ODQ3NF5BMl5BanBnXkFtZTgwNzY5NzMwMjE@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1914, 9, 15)
    ),
    Movie(
        id="ec61e0a8-0bf2-40da-8dd9-d3c72a9d207e", 
        title="The Jazz Singer",
        plot="The first feature-length motion picture with synchronized dialogue sequences.",
        year=1980, 
        directors=["Alan Crosland"],
        languages={"English", "Spanish"},
        imdb=Imdb(rating=7.0, votes=2000),
        poster="https://m.media-amazon.com/images/M/MV5BZGEwNTA3MjgtYzE0Mi00MjQ2LThkNjAtYzcyODE3NDBjODIwXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1980, 12, 19)
    ),
    Movie(
        id="7b6777a0-ff22-43c3-98a1-a58eff31d90b", 
        title="Salomé",
        plot="Salome, the daughter of Herodias, seduces her step-father/uncle Herod, governor of Judea, with a salacious dance. In return, he promises her the head of the prophet John the Baptist.", 
        year=1922, 
        directors=["Charles Bryant", "Alla Nazimova"],
        imdb=Imdb(rating=8.8, votes=3500),
        poster="https://m.media-amazon.com/images/M/MV5BMjA0MTY4MzI2OV5BMl5BanBnXkFtZTgwNTMyODg5MTE@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1923, 2, 15)
    ),
    Movie(
        id="3cdbb4a7-500e-4adb-9996-4cc2324a138c", 
        title="Wings", 
        year=1929, 
        directors=["William A. Wellman", "Harry d'Abbadie d'Arrast"],
        languages={"English", "Spanish", "French"},
        imdb=Imdb(rating=6.4, votes=2000),
        poster="https://m.media-amazon.com/images/M/MV5BYTI1YjgzZmMtZmIyYy00YTkwLTgyOWEtOTVlNTFkZmMzNTk3XkEyXkFqcGdeQXVyMDI2NDg0NQ@@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1929, 1, 5)
    ),
    Movie(
        id="ebcc5802-8efb-49f3-aa5c-58e007db5761", 
        title="The Phantom of the Opera", 
        year=1989, 
        directors=["Rupert Julian"],
        imdb=Imdb(rating=7.3, votes=4500),
        poster="https://m.media-amazon.com/images/M/MV5BMmUzMDFiMjItMDdmMS00MmVlLWEyODAtOTRhODZjZjEyYmM2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX677_AL_.jpg",
        released=datetime(1989, 11, 4)
    ),
    Movie(
        id="dd7262d0-a447-409c-8389-41c89db6a308", 
        title="The Gold Rush",
        plot="A lone prospector ventures into Alaska looking for gold and finds it and more.", 
        year=1925, 
        directors=["Charlie Chaplin"],
        languages={"English", "Spanish", "French", "German"},
        imdb=Imdb(rating=8.2, votes=5000)
    ),
    # 40 nuevas películas
    Movie(
        id=str(uuid4()), 
        title="Metropolis", 
        plot="In a futuristic city sharply divided between the working class and the city planners, the son of the city's mastermind falls in love with a working-class prophet.",
        year=1927, 
        directors=["Fritz Lang"],
        languages={"German", "English"},
        imdb=Imdb(rating=8.3, votes=6000),
        poster="https://m.media-amazon.com/images/M/MV5BMTg5YWIyMWUtZDY5My00ZmUtNDljNWE0NmI0NmM5M2E2NmUyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        released=datetime(1927, 1, 10)
    ),
    Movie(
        id=str(uuid4()), 
        title="Citizen Kane", 
        plot="Following the death of a publishing tycoon, news reporters scramble to discover the meaning of his final utterance.",
        year=1941, 
        directors=["Orson Welles"],
        languages={"English"},
        imdb=Imdb(rating=8.3, votes=7000),
        poster="https://m.media-amazon.com/images/M/MV5BYjBiOTYxZWItMzdiZi00NjlkLWIzZTYtYmFhZjhiMTljOTdkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1941, 5, 1)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Godfather", 
        plot="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        year=1972, 
        directors=["Francis Ford Coppola"],
        languages={"English", "Italian"},
        imdb=Imdb(rating=9.2, votes=12000),
        poster="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1972, 3, 24)
    ),
    Movie(
        id=str(uuid4()), 
        title="Pulp Fiction", 
        year=1994, 
        directors=["Quentin Tarantino"],
        languages={"English"},
        imdb=Imdb(rating=8.9, votes=15000),
        poster="https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzZiN2VkZjE3YzI0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1994, 10, 14)
    ),
    Movie(
        id=str(uuid4()), 
        title="Inception", 
        plot="A thief who steals corporate secrets through dream infiltration technology is given the task of planting an idea into the mind of a CEO.",
        year=2010, 
        directors=["Christopher Nolan"],
        languages={"English", "French"},
        imdb=Imdb(rating=8.8, votes=18000),
        poster="https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg",
        released=datetime(2010, 7, 16)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Shawshank Redemption", 
        year=1994, 
        directors=["Frank Darabont"],
        languages={"English"},
        imdb=Imdb(rating=9.3, votes=20000),
        poster="https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        released=datetime(1994, 9, 23)
    ),
    Movie(
        id=str(uuid4()), 
        title="Casablanca", 
        plot="A cynical expatriate American cafe owner struggles to decide whether or not to help his former lover and her fugitive husband escape the Nazis.",
        year=1942, 
        directors=["Michael Curtiz"],
        languages={"English", "French"},
        imdb=Imdb(rating=8.5, votes=8000),
        poster="https://m.media-amazon.com/images/M/MV5BY2IzZGY2YmEtYzljNS00NTM3LTgwMzAtMTkzYyI0NTcxY2M5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1942, 11, 26)
    ),
    Movie(
        id=str(uuid4()), 
        title="Star Wars: Episode IV - A New Hope", 
        year=1977, 
        directors=["George Lucas"],
        languages={"English"},
        imdb=Imdb(rating=8.6, votes=11000),
        poster="https://m.media-amazon.com/images/M/MV5BOTA5NjEyMTM5MF5BMl5BanBnXkFtZTcwMjYwMzY5Mw@@._V1_.jpg",
        released=datetime(1977, 5, 25)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Matrix", 
        plot="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        year=1999, 
        directors=["Lana Wachowski", "Lilly Wachowski"],
        languages={"English"},
        imdb=Imdb(rating=8.7, votes=14000),
        poster="https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
        released=datetime(1999, 3, 31)
    ),
    Movie(
        id=str(uuid4()), 
        title="Titanic", 
        year=1997, 
        directors=["James Cameron"],
        languages={"English", "French"},
        imdb=Imdb(rating=7.8, votes=9000),
        poster="https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",
        released=datetime(1997, 12, 19)
    ),
    Movie(
        id=str(uuid4()), 
        title="Psycho", 
        plot="A Phoenix secretary embezzles $40,000 and checks into a remote motel run by a young man under the domination of his mother.",
        year=1960, 
        directors=["Alfred Hitchcock"],
        languages={"English"},
        imdb=Imdb(rating=8.5, votes=6500),
        poster="https://m.media-amazon.com/images/M/MV5BNTQwNDM1YzItNDAxZC00NWY2LTk0M2UtNDIwNWI5OGUyNWY5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1960, 6, 16)
    ),
    Movie(
        id=str(uuid4()), 
        title="Gone with the Wind", 
        year=1939, 
        directors=["Victor Fleming"],
        languages={"English"},
        imdb=Imdb(rating=8.1, votes=5500),
        poster="https://m.media-amazon.com/images/M/MV5BYjUyZWZkM2UtMzYxYy00ZmQ3LWFmZTQtOGE2YjBkNjA3N2Y3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1939, 12, 15)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Lion King", 
        plot="Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
        year=1994, 
        directors=["Roger Allers", "Rob Minkoff"],
        languages={"English", "Swahili"},
        imdb=Imdb(rating=8.5, votes=10000),
        poster="https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2FjNmJjXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_.jpg",
        released=datetime(1994, 6, 15)
    ),
    Movie(
        id=str(uuid4()), 
        title="Jaws", 
        year=1975, 
        directors=["Steven Spielberg"],
        languages={"English"},
        imdb=Imdb(rating=8.0, votes=8500),
        poster="https://m.media-amazon.com/images/M/MV5BMmVmODY1MzEtYTMwZC00MzIyLThlYTMtN2Q0Y2UwZTRiYTgzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        released=datetime(1975, 6, 20)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Silence of the Lambs", 
        plot="A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to catch another serial killer.",
        year=1991, 
        directors=["Jonathan Demme"],
        languages={"English"},
        imdb=Imdb(rating=8.6, votes=13000),
        poster="https://m.media-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
        released=datetime(1991, 2, 14)
    ),
    Movie(
        id=str(uuid4()), 
        title="Forrest Gump", 
        year=1994, 
        directors=["Robert Zemeckis"],
        languages={"English"},
        imdb=Imdb(rating=8.8, votes=16000),
        poster="https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        released=datetime(1994, 7, 6)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Dark Knight", 
        plot="When the menace known as the Joker emerges, Batman must confront one of the greatest psychological and physical tests of his ability.",
        year=2008, 
        directors=["Christopher Nolan"],
        languages={"English"},
        imdb=Imdb(rating=9.0, votes=19000),
        poster="https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
        released=datetime(2008, 7, 18)
    ),
    Movie(
        id=str(uuid4()), 
        title="Schindler's List", 
        year=1993, 
        directors=["Steven Spielberg"],
        languages={"English", "German"},
        imdb=Imdb(rating=8.9, votes=14000),
        poster="https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
        released=datetime(1993, 12, 15)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Empire Strikes Back", 
        plot="After the Rebels are brutally overpowered by the Empire, Luke Skywalker begins Jedi training with Yoda.",
        year=1980, 
        directors=["Irvin Kershner"],
        languages={"English"},
        imdb=Imdb(rating=8.7, votes=12000),
        poster="https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1980, 5, 21)
    ),
    Movie(
        id=str(uuid4()), 
        title="Goodfellas", 
        year=1990, 
        directors=["Martin Scorsese"],
        languages={"English", "Italian"},
        imdb=Imdb(rating=8.7, votes=11000),
        poster="https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjIwYjFjNmI3ZGEwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1990, 9, 19)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Lord of the Rings: The Fellowship of the Ring", 
        plot="A meek Hobbit and eight companions set out on a journey to destroy a powerful ring and save Middle-earth.",
        year=2001, 
        directors=["Peter Jackson"],
        languages={"English"},
        imdb=Imdb(rating=8.8, votes=17000),
        poster="https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_.jpg",
        released=datetime(2001, 12, 19)
    ),
    Movie(
        id=str(uuid4()), 
        title="Fight Club", 
        year=1999, 
        directors=["David Fincher"],
        languages={"English"},
        imdb=Imdb(rating=8.8, votes=15000),
        poster="https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        released=datetime(1999, 10, 15)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Avengers", 
        plot="Earth's mightiest heroes must come together to stop Loki and his alien army from enslaving humanity.",
        year=2012, 
        directors=["Joss Whedon"],
        languages={"English"},
        imdb=Imdb(rating=8.0, votes=13000),
        poster="https://m.media-amazon.com/images/M/MV5BNDYxNjU3Mzc5NF5BMl5BanBnXkFtZTcwODY5NjMwNw@@._V1_.jpg",
        released=datetime(2012, 5, 4)
    ),
    Movie(
        id=str(uuid4()), 
        title="Parasite", 
        plot="Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        year=2019, 
        directors=["Bong Joon-ho"],
        languages={"Korean", "English"},
        imdb=Imdb(rating=8.6, votes=12000),
        poster="https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg",
        released=datetime(2019, 5, 30)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Wizard of Oz", 
        year=1939, 
        directors=["Victor Fleming"],
        languages={"English"},
        imdb=Imdb(rating=8.0, votes=6000),
        poster="https://m.media-amazon.com/images/M/MV5BNjUyMTc4MDExMV5BMl5BanBnXkFtZTgwNDg0NDIwMjE@._V1_.jpg",
        released=datetime(1939, 8, 25)
    ),
    Movie(
        id=str(uuid4()), 
        title="E.T. the Extra-Terrestrial", 
        plot="A troubled child summons the courage to help a friendly alien escape Earth and return to his home planet.",
        year=1982, 
        directors=["Steven Spielberg"],
        languages={"English"},
        imdb=Imdb(rating=7.8, votes=9000),
        poster="https://m.media-amazon.com/images/M/MV5BMTQ2ODFlMDAtNzdhOC00ZDYzLWE3YTMtNDU4ZGFmZmJmYTczXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        released=datetime(1982, 6, 11)
    ),
    Movie(
        id=str(uuid4()), 
        title="Jurassic Park", 
        year=1993, 
        directors=["Steven Spielberg"],
        languages={"English", "Spanish"},
        imdb=Imdb(rating=8.1, votes=11000),
        poster="https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2MjAwMDE@._V1_.jpg",
        released=datetime(1993, 6, 11)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Exorcist", 
        plot="When a teenage girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her.",
        year=1973, 
        directors=["William Friedkin"],
        languages={"English"},
        imdb=Imdb(rating=8.0, votes=7500),
        poster="https://m.media-amazon.com/images/M/MV5BYWFlZGY2NDktY2ZjOS00ZWNkLTg0ZDAtZDY4MTM1ODU4ZjljXkEyXkFqcGdeQXVyMjUzOTY1NTY@._V1_.jpg",
        released=datetime(1973, 12, 26)
    ),
    Movie(
        id=str(uuid4()), 
        title="Back to the Future", 
        year=1985, 
        directors=["Robert Zemeckis"],
        languages={"English"},
        imdb=Imdb(rating=8.5, votes=12000),
        poster="https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        released=datetime(1985, 7, 3)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Shining", 
        plot="A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence.",
        year=1980, 
        directors=["Stanley Kubrick"],
        languages={"English"},
        imdb=Imdb(rating=8.4, votes=10000),
        poster="https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        released=datetime(1980, 5, 23)
    ),
    Movie(
        id=str(uuid4()), 
        title="Gladiator", 
        year=2000, 
        directors=["Ridley Scott"],
        languages={"English"},
        imdb=Imdb(rating=8.5, votes=14000),
        poster="https://m.media-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGE5NjEzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        released=datetime(2000, 5, 5)
    ),
    Movie(
        id=str(uuid4()), 
        title="The Departed", 
        plot="An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang.",
        year=2006, 
        directors=["Martin Scorsese"],
        languages={"English"},
        imdb=Imdb(rating=8.5, votes=13000),
        poster="https://m.media-amazon.com/images/M/MV5BMTI1MTYxOTAwM15BMl5BanBnXkFtZTcwNTc2MjM2MQ@@._V1_.jpg",
        released=datetime(2006, 10, 6)
    ),
    Movie(
        id=str(uuid4()), 
        title="La La Land", 
        year=2016, 
        directors=["Damien Chazelle"],
        languages={"English"},
        imdb=Imdb(rating=8.0, votes=11000),
        poster="https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg",
        released=datetime(2016, 12, 9)
    ),
    Movie(
        id=str(uuid4()), 
        title="Mad Max: Fury Road", 
        plot="In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland.",
        year=2015, 
        directors=["George Miller"],
        languages={"English"},
        imdb=Imdb(rating=8.1, votes=12000),
        poster="https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwMmI3XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        released=datetime(2015, 5, 15)
    ),
    Movie(
        id=str(uuid4()), 
        title="Whiplash", 
        year=2014, 
        directors=["Damien Chazelle"],
        languages={"English"},
        imdb=Imdb(rating=8.5, votes=10000),
        poster="https://m.media-amazon.com/images/M/MV5BOTA5NDYxNTg0OV5BMl5BanBnXkFtZTgwODE5NzU1MTE@._V1_.jpg",
        released=datetime(2014, 10, 10)
    ),
]

# Para verificar
if __name__ == "__main__":
    print(f"Total de películas: {len(MOVIES_LIST)}")
    for movie in MOVIES_LIST:
        print(movie)