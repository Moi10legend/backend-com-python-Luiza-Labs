import bcrypt
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from typing import Optional
from jose import jwt

SECRET_KEY = "my-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_password_hash(password: str) -> str:
    # O bcrypt pede a senha em bytes, então fazemos .encode()
    pwd_bytes = password.encode('utf-8')
    
    # Gera o salt
    salt = bcrypt.gensalt()
    
    # Gera o hash
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    
    # Retornamos como string para salvar no banco de dados
    return hashed_password.decode('utf-8')

# 2. Função para verificar a senha
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Convertemos ambas para bytes antes de comparar
    pwd_bytes = plain_password.encode('utf-8')
    hash_bytes = hashed_password.encode('utf-8')
    
    return bcrypt.checkpw(pwd_bytes, hash_bytes)

# 3. Função para criar o Token (Essa não muda nada)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(ZoneInfo("America/Recife")) + expires_delta
    else:
        expire = datetime.now(ZoneInfo("America/Recife")) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt