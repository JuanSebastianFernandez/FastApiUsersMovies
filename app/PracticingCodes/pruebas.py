class User():
    def __init__(self, id:int, name:str, email:str, password:str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}, password: {self.password}"


users_list = [
    User(id=1, name="Juan Perez", email="juan_peres@gmail.com", password="123456"),
    User(id=2, name="Maria Lopez", email="maria_lopez@gmail.com", password="654312"),
    User(id=3, name="Carlos Perez", email="CarlosPerez@hotmail.com", password="5478621"),
    User(id=4, name="Ana Maria", email="Mana@hotmail.com", password="123456"),
    User(id=5, name="Jose Perez", email="Perezpereza@gmail.com", password="253698")
]


def search_user_by_id(id:int):
    search_user = next((user for user in users_list if user.id == id), None)
    return search_user or "Not found"

def read_items(q:str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results

print(read_items({"algo":"cualquier cosa", "otro":"otra cosa"}))