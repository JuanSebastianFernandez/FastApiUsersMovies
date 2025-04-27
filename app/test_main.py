from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", data={"username": "juan_peres@gmail.com", "password": "123456"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_failure_wrong_password():
    response = client.post(
        "/login/",
        data={"username": "benjamin.perez@gmail.com", "password": "contraseña_incorrecta"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect email or password"

def test_read_users():
    response = client.get("/users/?start=69&limit=5&show_password=True")
    assert response.status_code == 200
    assert len(response.json()) == 5
    assert "password" in response.json()[0]
    assert response.json() == [
    {
        "id": 70,
        "email": "carmen.rojas@hotmail.com",
        "name": "Carmen Rojas",
        "password": "$2b$12$/3noPdxVNJBdNUydxm8PfutzqCVYiLsXjefNRzRC0k.7QyenydFGC"
    },
    {
        "id": 71,
        "email": "agustin_castro@live.com",
        "name": "Agustin Castro",
        "password": "$2b$12$HTxJLd0U2yx78L870WGmcuJph1G9vREtT2sZO/hA6.xwoMk1cVKum"
    },
    {
        "id": 72,
        "email": "olivia.ortiz@yahoo.com",
        "name": "Olivia Ortiz",
        "password": "$2b$12$tUDYFrD9L6qD3ZArW1dV4e561.0gLo9ogGJxAk0fjCyxlfUhKwM.2"
    },
    {
        "id": 73,
        "email": "ramiro_vega@gmail.com",
        "name": "Ramiro Vega",
        "password": "$2b$12$mw7.k.ZvkqGxOPEGrBTKHu1qWj93DKjVPZWAuRMMRIEs.8mcea9q2"
    },
    {
        "id": 74,
        "email": "victoria.morales@outlook.com",
        "name": "Victoria Morales",
        "password": "$2b$12$8Fb7KmtrnoBq0IPahpZo9.9NwPhEuu7D07NiQE2Bqi82NC..uhfpC"
    }
    ]


def test_read_user():
    response = client.get("/users/45")
    assert response.status_code == 200
    assert response.json() == {
        "message": "User found",
        "user": {
            "name": "Benjamin Perez",
            "email": "benjamin.perez@gmail.com",
            "id": 45
            }
        }

def test_read_user_me():
    # Paso 1: Loguearse
    login_response = client.post("/login", data={"username": "juan_peres@gmail.com", "password": "123456"})
    assert login_response.status_code == 200
    acces_token = login_response.json()["access_token"]

    # Paso 2: Llamar a /users/me con el token
    headers = {
        "Authorization": f"Bearer {acces_token}"
    }
    me_response = client.get("/users/me", headers=headers)
    assert me_response.status_code == 200

    # Paso 3: Verificar que sea el usuario correcto
    user_data = me_response.json()
    assert user_data["email"] == "juan_peres@gmail.com"
    assert user_data["name"] == "Juan Perez"
    assert user_data["id"] == 1

def test_create_user():
    new_user = {
        "name": "Test User",
        "email": "testuser@gmail.com",
        "password": "testpassword"
    }
    response = client.post("/users/", json=new_user)
    assert response.status_code == 200
    assert response.json()["message"] == "User Created Successfully"
    assert response.json()["user"]["email"] == new_user["email"]


def test_get_favorite_movie():
    headers = {
        "X-Token": "secreto123"
    }
    response = client.get("/movies/favorite/680e89f08c22fb3659b5e0ee", headers=headers)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Movie 680e89f08c22fb3659b5e0ee set as favorite"
    }
    assert response.cookies["favorite_movie"] == "680e89f08c22fb3659b5e0ee"