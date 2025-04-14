import hashlib

def hash_password(password: str) -> str:
    # Codificamos la contraseña a bytes
    password_bytes = password.encode('utf-8')
    
    # Usamos SHA-256 para hacer el hash
    hashed = hashlib.sha256(password_bytes).hexdigest()
    
    return hashed