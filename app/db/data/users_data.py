# Base de datos simulada

USER_LIST = []

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
    from app.db.models.users_models import UserInDB
    from app.core.security import hash_password
    from app.db.clientsql import create_db_and_tables, engine
    from sqlmodel import Session

    create_db_and_tables()

    USER_LIST = [
    UserInDB(name="Juan Perez", email="juan_peres@gmail.com", password=hash_password("123456")),
    UserInDB(name="Maria Lopez", email="maria_lopez@gmail.com", password=hash_password("654312")),
    UserInDB(name="Carlos Perez", email="CarlosPerez@hotmail.com", password=hash_password("5478621")),
    UserInDB(name="Ana Maria", email="Mana@hotmail.com", password=hash_password("123456")),
    UserInDB(name="Jose Perez", email="Perezpereza@gmail.com", password=hash_password("253698")),
    UserInDB(name="Laura Gomez", email="laura_gomez@yahoo.com", password=hash_password("789123")),
    UserInDB(name="Pedro Sanchez", email="pedro.sanchez@outlook.com", password=hash_password("456789")),
    UserInDB(name="Sofia Ramirez", email="sofia_ramirez@gmail.com", password=hash_password("321654")),
    UserInDB(name="Luis Torres", email="luist@hotmail.com", password=hash_password("987654")),
    UserInDB(name="Clara Ortiz", email="clara.ortiz@live.com", password=hash_password("147258")),
    UserInDB(name="Diego Morales", email="diego_morales@gmail.com", password=hash_password("369852")),
    UserInDB(name="Elena Castro", email="elena.castro@yahoo.com", password=hash_password("258963")),
    UserInDB(name="Miguel Angel", email="miguel_angel@outlook.com", password=hash_password("741852")),
    UserInDB(name="Valeria Diaz", email="valeria.diaz@gmail.com", password=hash_password("852963")),
    UserInDB(name="Andres Ruiz", email="andresruiz@hotmail.com", password=hash_password("159357")),
    UserInDB(name="Camila Vargas", email="camila.vargas@yahoo.com", password=hash_password("753951")),
    UserInDB(name="Javier Mendez", email="javier_mendez@live.com", password=hash_password("456123")),
    UserInDB(name="Paula Herrera", email="paula.herrera@gmail.com", password=hash_password("789456")),
    UserInDB(name="Ricardo Silva", email="ricardo_silva@outlook.com", password=hash_password("321987")),
    UserInDB(name="Isabela Cruz", email="isabela.cruz@yahoo.com", password=hash_password("654789")),
    UserInDB(name="Gabriel Luna", email="gabriel_luna@gmail.com", password=hash_password("123789")),
    UserInDB(name="Natalia Rojas", email="natalia.rojas@live.com", password=hash_password("987321")),
    UserInDB(name="Felipe Castro", email="felipe_castro@hotmail.com", password=hash_password("456321")),
    UserInDB(name="Daniela Ortiz", email="daniela.ortiz@yahoo.com", password=hash_password("789654")),
    UserInDB(name="Alejandro Vega", email="alejandro_vega@gmail.com", password=hash_password("147963")),
    UserInDB(name="Lucia Morales", email="lucia.morales@outlook.com", password=hash_password("258741")),
    UserInDB(name="Mateo Gomez", email="mateo_gomez@hotmail.com", password=hash_password("369147")),
    UserInDB(name="Sara Lopez", email="sara_lopez@yahoo.com", password=hash_password("852741")),
    UserInDB(name="Julian Perez", email="julian.perez@gmail.com", password=hash_password("963258")),
    UserInDB(name="Carolina Diaz", email="carolina_diaz@live.com", password=hash_password("741369")),
    UserInDB(name="Sebastian Ruiz", email="sebastian.ruiz@outlook.com", password=hash_password("159852")),
    UserInDB(name="Emma Torres", email="emma_torres@yahoo.com", password=hash_password("357951")),
    UserInDB(name="Tomas Sanchez", email="tomas_sanchez@gmail.com", password=hash_password("456852")),
    UserInDB(name="Renata Vargas", email="renata.vargas@hotmail.com", password=hash_password("789321")),
    UserInDB(name="Nicolas Mendez", email="nicolas_mendez@live.com", password=hash_password("123654")),
    UserInDB(name="Valentina Cruz", email="valentina.cruz@yahoo.com", password=hash_password("987456")),
    UserInDB(name="Santiago Luna", email="santiago_luna@gmail.com", password=hash_password("321456")),
    UserInDB(name="Mariana Rojas", email="mariana.rojas@outlook.com", password=hash_password("654123")),
    UserInDB(name="Emiliano Castro", email="emiliano_castro@hotmail.com", password=hash_password("789123")),
    UserInDB(name="Catalina Ortiz", email="catalina.ortiz@yahoo.com", password=hash_password("456987")),
    UserInDB(name="Martin Vega", email="martin_vega@gmail.com", password=hash_password("147258")),
    UserInDB(name="Florencia Morales", email="florencia.morales@live.com", password=hash_password("369852")),
    UserInDB(name="Ignacio Gomez", email="ignacio_gomez@outlook.com", password=hash_password("258963")),
    UserInDB(name="Agustina Lopez", email="agustina_lopez@yahoo.com", password=hash_password("741852")),
    UserInDB(name="Benjamin Perez", email="benjamin.perez@gmail.com", password=hash_password("852963")),
    UserInDB(name="Luz Diaz", email="luz_diaz@hotmail.com", password=hash_password("159357")),
    UserInDB(name="Thiago Ruiz", email="thiago.ruiz@live.com", password=hash_password("753951")),
    UserInDB(name="Antonella Torres", email="antonella_torres@yahoo.com", password=hash_password("456123")),
    UserInDB(name="Lorenzo Sanchez", email="lorenzo_sanchez@gmail.com", password=hash_password("789456")),
    UserInDB(name="Pia Vargas", email="pia.vargas@outlook.com", password=hash_password("321987")),
    UserInDB(name="Bruno Mendez", email="bruno_mendez@hotmail.com", password=hash_password("654789")),
    UserInDB(name="Delfina Cruz", email="delfina.cruz@yahoo.com", password=hash_password("123789")),
    UserInDB(name="Facundo Luna", email="facundo_luna@gmail.com", password=hash_password("987321")),
    UserInDB(name="Juana Rojas", email="juana.rojas@live.com", password=hash_password("456321")),
    UserInDB(name="Roman Castro", email="roman_castro@outlook.com", password=hash_password("789654")),
    UserInDB(name="Milagros Ortiz", email="milagros.ortiz@yahoo.com", password=hash_password("147963")),
    UserInDB(name="Ezequiel Vega", email="ezequiel_vega@gmail.com", password=hash_password("258741")),
    UserInDB(name="Candela Morales", email="candela.morales@hotmail.com", password=hash_password("369147")),
    UserInDB(name="Joaquin Gomez", email="joaquin_gomez@live.com", password=hash_password("852741")),
    UserInDB(name="Belen Lopez", email="belen_lopez@yahoo.com", password=hash_password("963258")),
    UserInDB(name="Matias Perez", email="matias.perez@gmail.com", password=hash_password("741369")),
    UserInDB(name="Rocio Diaz", email="rocio_diaz@outlook.com", password=hash_password("159852")),
    UserInDB(name="Lautaro Ruiz", email="lautaro.ruiz@hotmail.com", password=hash_password("357951")),
    UserInDB(name="Sol Torres", email="sol_torres@yahoo.com", password=hash_password("456852")),
    UserInDB(name="Gonzalo Sanchez", email="gonzalo_sanchez@gmail.com", password=hash_password("789321")),
    UserInDB(name="Martina Vargas", email="martina.vargas@live.com", password=hash_password("123654")),
    UserInDB(name="Leandro Mendez", email="leandro_mendez@outlook.com", password=hash_password("987456")),
    UserInDB(name="Abril Cruz", email="abril.cruz@yahoo.com", password=hash_password("321456")),
    UserInDB(name="Franco Luna", email="franco_luna@gmail.com", password=hash_password("654123")),
    UserInDB(name="Carmen Rojas", email="carmen.rojas@hotmail.com", password=hash_password("789123")),
    UserInDB(name="Agustin Castro", email="agustin_castro@live.com", password=hash_password("456987")),
    UserInDB(name="Olivia Ortiz", email="olivia.ortiz@yahoo.com", password=hash_password("147258")),
    UserInDB(name="Ramiro Vega", email="ramiro_vega@gmail.com", password=hash_password("369852")),
    UserInDB(name="Victoria Morales", email="victoria.morales@outlook.com", password=hash_password("258963")),
    UserInDB(name="Pablo Gomez", email="pablo_gomez@hotmail.com", password=hash_password("741852")),
    UserInDB(name="Alicia Lopez", email="alicia_lopez@yahoo.com", password=hash_password("852963")),
    UserInDB(name="Hugo Perez", email="hugo.perez@gmail.com", password=hash_password("159357")),
    UserInDB(name="Elena Diaz", email="elena_diaz@live.com", password=hash_password("753951")),
    UserInDB(name="Marcos Ruiz", email="marcos.ruiz@outlook.com", password=hash_password("456123")),
    UserInDB(name="Julia Torres", email="julia_torres@yahoo.com", password=hash_password("789456")),
]
    
    with Session(engine) as session:
        for user in USER_LIST:
            session.add(user)
        session.commit()
        