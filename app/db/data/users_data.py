import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))      # db/
root_dir   = os.path.abspath(os.path.join(current_dir, '../..'))   # raíz del proyecto

# Agregar ambos
sys.path.append(parent_dir)
sys.path.append(root_dir)

from models.users_models import UserInDB
from bson import ObjectId
from core.security import hash_password


# Base de datos simulada
USER_LIST = [
    UserInDB(id=str(ObjectId()), name="Juan Perez", email="juan_peres@gmail.com", hashed_password=hash_password("123456")),
    UserInDB(id=str(ObjectId()), name="Maria Lopez", email="maria_lopez@gmail.com", hashed_password=hash_password("654312")),
    UserInDB(id=str(ObjectId()), name="Carlos Perez", email="CarlosPerez@hotmail.com", hashed_password=hash_password("5478621")),
    UserInDB(id=str(ObjectId()), name="Ana Maria", email="Mana@hotmail.com", hashed_password=hash_password("123456")),
    UserInDB(id=str(ObjectId()), name="Jose Perez", email="Perezpereza@gmail.com", hashed_password=hash_password("253698")),
    UserInDB(id=str(ObjectId()), name="Laura Gomez", email="laura_gomez@yahoo.com", hashed_password=hash_password("789123")),
    UserInDB(id=str(ObjectId()), name="Pedro Sanchez", email="pedro.sanchez@outlook.com", hashed_password=hash_password("456789")),
    UserInDB(id=str(ObjectId()), name="Sofia Ramirez", email="sofia_ramirez@gmail.com", hashed_password=hash_password("321654")),
    UserInDB(id=str(ObjectId()), name="Luis Torres", email="luist@hotmail.com", hashed_password=hash_password("987654")),
    UserInDB(id=str(ObjectId()), name="Clara Ortiz", email="clara.ortiz@live.com", hashed_password=hash_password("147258")),
    UserInDB(id=str(ObjectId()), name="Diego Morales", email="diego_morales@gmail.com", hashed_password=hash_password("369852")),
    UserInDB(id=str(ObjectId()), name="Elena Castro", email="elena.castro@yahoo.com", hashed_password=hash_password("258963")),
    UserInDB(id=str(ObjectId()), name="Miguel Angel", email="miguel_angel@outlook.com", hashed_password=hash_password("741852")),
    UserInDB(id=str(ObjectId()), name="Valeria Diaz", email="valeria.diaz@gmail.com", hashed_password=hash_password("852963")),
    UserInDB(id=str(ObjectId()), name="Andres Ruiz", email="andresruiz@hotmail.com", hashed_password=hash_password("159357")),
    UserInDB(id=str(ObjectId()), name="Camila Vargas", email="camila.vargas@yahoo.com", hashed_password=hash_password("753951")),
    UserInDB(id=str(ObjectId()), name="Javier Mendez", email="javier_mendez@live.com", hashed_password=hash_password("456123")),
    UserInDB(id=str(ObjectId()), name="Paula Herrera", email="paula.herrera@gmail.com", hashed_password=hash_password("789456")),
    UserInDB(id=str(ObjectId()), name="Ricardo Silva", email="ricardo_silva@outlook.com", hashed_password=hash_password("321987")),
    UserInDB(id=str(ObjectId()), name="Isabela Cruz", email="isabela.cruz@yahoo.com", hashed_password=hash_password("654789")),
    UserInDB(id=str(ObjectId()), name="Gabriel Luna", email="gabriel_luna@gmail.com", hashed_password=hash_password("123789")),
    UserInDB(id=str(ObjectId()), name="Natalia Rojas", email="natalia.rojas@live.com", hashed_password=hash_password("987321")),
    UserInDB(id=str(ObjectId()), name="Felipe Castro", email="felipe_castro@hotmail.com", hashed_password=hash_password("456321")),
    UserInDB(id=str(ObjectId()), name="Daniela Ortiz", email="daniela.ortiz@yahoo.com", hashed_password=hash_password("789654")),
    UserInDB(id=str(ObjectId()), name="Alejandro Vega", email="alejandro_vega@gmail.com", hashed_password=hash_password("147963")),
    UserInDB(id=str(ObjectId()), name="Lucia Morales", email="lucia.morales@outlook.com", hashed_password=hash_password("258741")),
    UserInDB(id=str(ObjectId()), name="Mateo Gomez", email="mateo_gomez@hotmail.com", hashed_password=hash_password("369147")),
    UserInDB(id=str(ObjectId()), name="Sara Lopez", email="sara_lopez@yahoo.com", hashed_password=hash_password("852741")),
    UserInDB(id=str(ObjectId()), name="Julian Perez", email="julian.perez@gmail.com", hashed_password=hash_password("963258")),
    UserInDB(id=str(ObjectId()), name="Carolina Diaz", email="carolina_diaz@live.com", hashed_password=hash_password("741369")),
    UserInDB(id=str(ObjectId()), name="Sebastian Ruiz", email="sebastian.ruiz@outlook.com", hashed_password=hash_password("159852")),
    UserInDB(id=str(ObjectId()), name="Emma Torres", email="emma_torres@yahoo.com", hashed_password=hash_password("357951")),
    UserInDB(id=str(ObjectId()), name="Tomas Sanchez", email="tomas_sanchez@gmail.com", hashed_password=hash_password("456852")),
    UserInDB(id=str(ObjectId()), name="Renata Vargas", email="renata.vargas@hotmail.com", hashed_password=hash_password("789321")),
    UserInDB(id=str(ObjectId()), name="Nicolas Mendez", email="nicolas_mendez@live.com", hashed_password=hash_password("123654")),
    UserInDB(id=str(ObjectId()), name="Valentina Cruz", email="valentina.cruz@yahoo.com", hashed_password=hash_password("987456")),
    UserInDB(id=str(ObjectId()), name="Santiago Luna", email="santiago_luna@gmail.com", hashed_password=hash_password("321456")),
    UserInDB(id=str(ObjectId()), name="Mariana Rojas", email="mariana.rojas@outlook.com", hashed_password=hash_password("654123")),
    UserInDB(id=str(ObjectId()), name="Emiliano Castro", email="emiliano_castro@hotmail.com", hashed_password=hash_password("789123")),
    UserInDB(id=str(ObjectId()), name="Catalina Ortiz", email="catalina.ortiz@yahoo.com", hashed_password=hash_password("456987")),
    UserInDB(id=str(ObjectId()), name="Martin Vega", email="martin_vega@gmail.com", hashed_password=hash_password("147258")),
    UserInDB(id=str(ObjectId()), name="Florencia Morales", email="florencia.morales@live.com", hashed_password=hash_password("369852")),
    UserInDB(id=str(ObjectId()), name="Ignacio Gomez", email="ignacio_gomez@outlook.com", hashed_password=hash_password("258963")),
    UserInDB(id=str(ObjectId()), name="Agustina Lopez", email="agustina_lopez@yahoo.com", hashed_password=hash_password("741852")),
    UserInDB(id=str(ObjectId()), name="Benjamin Perez", email="benjamin.perez@gmail.com", hashed_password=hash_password("852963")),
    UserInDB(id=str(ObjectId()), name="Luz Diaz", email="luz_diaz@hotmail.com", hashed_password=hash_password("159357")),
    UserInDB(id=str(ObjectId()), name="Thiago Ruiz", email="thiago.ruiz@live.com", hashed_password=hash_password("753951")),
    UserInDB(id=str(ObjectId()), name="Antonella Torres", email="antonella_torres@yahoo.com", hashed_password=hash_password("456123")),
    UserInDB(id=str(ObjectId()), name="Lorenzo Sanchez", email="lorenzo_sanchez@gmail.com", hashed_password=hash_password("789456")),
    UserInDB(id=str(ObjectId()), name="Pia Vargas", email="pia.vargas@outlook.com", hashed_password=hash_password("321987")),
    UserInDB(id=str(ObjectId()), name="Bruno Mendez", email="bruno_mendez@hotmail.com", hashed_password=hash_password("654789")),
    UserInDB(id=str(ObjectId()), name="Delfina Cruz", email="delfina.cruz@yahoo.com", hashed_password=hash_password("123789")),
    UserInDB(id=str(ObjectId()), name="Facundo Luna", email="facundo_luna@gmail.com", hashed_password=hash_password("987321")),
    UserInDB(id=str(ObjectId()), name="Juana Rojas", email="juana.rojas@live.com", hashed_password=hash_password("456321")),
    UserInDB(id=str(ObjectId()), name="Roman Castro", email="roman_castro@outlook.com", hashed_password=hash_password("789654")),
    UserInDB(id=str(ObjectId()), name="Milagros Ortiz", email="milagros.ortiz@yahoo.com", hashed_password=hash_password("147963")),
    UserInDB(id=str(ObjectId()), name="Ezequiel Vega", email="ezequiel_vega@gmail.com", hashed_password=hash_password("258741")),
    UserInDB(id=str(ObjectId()), name="Candela Morales", email="candela.morales@hotmail.com", hashed_password=hash_password("369147")),
    UserInDB(id=str(ObjectId()), name="Joaquin Gomez", email="joaquin_gomez@live.com", hashed_password=hash_password("852741")),
    UserInDB(id=str(ObjectId()), name="Belen Lopez", email="belen_lopez@yahoo.com", hashed_password=hash_password("963258")),
    UserInDB(id=str(ObjectId()), name="Matias Perez", email="matias.perez@gmail.com", hashed_password=hash_password("741369")),
    UserInDB(id=str(ObjectId()), name="Rocio Diaz", email="rocio_diaz@outlook.com", hashed_password=hash_password("159852")),
    UserInDB(id=str(ObjectId()), name="Lautaro Ruiz", email="lautaro.ruiz@hotmail.com", hashed_password=hash_password("357951")),
    UserInDB(id=str(ObjectId()), name="Sol Torres", email="sol_torres@yahoo.com", hashed_password=hash_password("456852")),
    UserInDB(id=str(ObjectId()), name="Gonzalo Sanchez", email="gonzalo_sanchez@gmail.com", hashed_password=hash_password("789321")),
    UserInDB(id=str(ObjectId()), name="Martina Vargas", email="martina.vargas@live.com", hashed_password=hash_password("123654")),
    UserInDB(id=str(ObjectId()), name="Leandro Mendez", email="leandro_mendez@outlook.com", hashed_password=hash_password("987456")),
    UserInDB(id=str(ObjectId()), name="Abril Cruz", email="abril.cruz@yahoo.com", hashed_password=hash_password("321456")),
    UserInDB(id=str(ObjectId()), name="Franco Luna", email="franco_luna@gmail.com", hashed_password=hash_password("654123")),
    UserInDB(id=str(ObjectId()), name="Carmen Rojas", email="carmen.rojas@hotmail.com", hashed_password=hash_password("789123")),
    UserInDB(id=str(ObjectId()), name="Agustin Castro", email="agustin_castro@live.com", hashed_password=hash_password("456987")),
    UserInDB(id=str(ObjectId()), name="Olivia Ortiz", email="olivia.ortiz@yahoo.com", hashed_password=hash_password("147258")),
    UserInDB(id=str(ObjectId()), name="Ramiro Vega", email="ramiro_vega@gmail.com", hashed_password=hash_password("369852")),
    UserInDB(id=str(ObjectId()), name="Victoria Morales", email="victoria.morales@outlook.com", hashed_password=hash_password("258963")),
    UserInDB(id=str(ObjectId()), name="Pablo Gomez", email="pablo_gomez@hotmail.com", hashed_password=hash_password("741852")),
    UserInDB(id=str(ObjectId()), name="Alicia Lopez", email="alicia_lopez@yahoo.com", hashed_password=hash_password("852963")),
    UserInDB(id=str(ObjectId()), name="Hugo Perez", email="hugo.perez@gmail.com", hashed_password=hash_password("159357")),
    UserInDB(id=str(ObjectId()), name="Elena Diaz", email="elena_diaz@live.com", hashed_password=hash_password("753951")),
    UserInDB(id=str(ObjectId()), name="Marcos Ruiz", email="marcos.ruiz@outlook.com", hashed_password=hash_password("456123")),
    UserInDB(id=str(ObjectId()), name="Julia Torres", email="julia_torres@yahoo.com", hashed_password=hash_password("789456"))
]

if __name__ == "__main__":
    for user in USER_LIST:
        print(user)