from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt

ALGORITHM = "HS256"
SECRET_KEY = "b45837f062e096e742cffd60176d1eaf08b8b3b1b4347c6c774e4453a424d723" # Generado con gitbash $ openssl rand -hex 32, se podría guardar en memoria del pc para no dejaro en crudo en el código

# --------------------- Contexto de encriptación de contraseñas ---------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_acces_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encode_jwt

def decode_acces_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


if __name__ == "__main__":
    # Ejemplo de uso
    password = "mi_contraseña_secreta"
    hashed_password = hash_password(password)
    print(f"Contraseña original: {password}")
    print(f"Contraseña hasheada: {hashed_password}")
    print(verify_password(password, hashed_password))
    data = {"sub":"101546987436554", "email":"juanito_1996@hotmail.com"}
    token = create_acces_token(data)
    print(token)
    print(decode_acces_token(token))