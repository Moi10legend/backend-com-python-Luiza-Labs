from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Annotated
from database import get_session
from src.models.account import Account
from security import verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter(prefix="/account")

# Schema simples para a resposta do Token (pode ir para schemas.py depois)
class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(get_session)]
):
    # 1. Buscar o usuário pelo nome (que atua como username)
    # O OAuth2PasswordRequestForm sempre envia os campos 'username' e 'password'
    query = select(Account).where(Account.name == form_data.username)
    result = await session.exec(query)
    account = result.first()

    # 2. Verificar se o usuário existe e se a senha bate
    if not account or not verify_password(form_data.password, account.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Gerar o Token de Acesso
    # O 'sub' (subject) no token geralmente é o ID do usuário convertido para string
    access_token = create_access_token(data={"sub": str(account.id)})
    
    # 4. Retornar o token
    return {"access_token": access_token, "token_type": "bearer"}