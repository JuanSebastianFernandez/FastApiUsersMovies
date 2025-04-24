from app.db.models.users_models import UserIn, UserInDB
from app.core.security import hash_password
from sqlmodel import Session, select

#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_user(session: Session, id:int|None, email:str = None) ->  UserInDB|None:

    if id is not None:
        return session.get(UserInDB, id)
    
    if email is not None:
        statement = select(UserInDB).where(UserInDB.email == email)
        return session.exec(statement).first()
    
    return None  # Si no se pasa ni id ni email

def save_user(user_in:UserIn):
    user_in.password = hash_password(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump())
    
    return user_in_db

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)
        
if __name__ == "__main__":
    # How testing from cmd or powershell / bash from root -> python -m app.core.user_service
    print("Testing search_user:")
    user_found = search_user(id=None, email="juan_peres@gmail.com")
    if user_found:
        print(dict(user_found[1]))
    else:
        print(user_found)
    print("---"*15)
    print("Testing save_user:")
    new_user = save_user(UserIn(
        id="123456789", 
        name="Juan Fernandez", 
        email="juab@test.com", 
        password="Mypassword123"))
    print(dict(new_user))


