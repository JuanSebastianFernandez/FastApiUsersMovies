from app.db.models.users_models import UserIn, UserInDB
from app.db.data.users_data import USER_LIST as users_list
from app.db.data.users_data import hash_password
#---------------------------------------------- Definición de funciones auxiliares -----------------------------------------------

def search_user(id:str|None, email:str = None) -> tuple[int, UserInDB]|None:
    for index, search_user in enumerate(users_list):
        if search_user.id == id or search_user.email == email:
            return index, search_user
    return None

def save_user(user_in:UserIn):
    hashed_password = hash_password(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    
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


