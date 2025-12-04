from fastapi import status, APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from src.schemas.AccountIn import AccountIn
from src.schemas.TransactionsReadIn import TransactionsReadIn
from src.schemas.TransactionCreate import TransactionCreate
from src.views.AccountOut import AccountOut
from src.views.TransactionReadOut import TransactionReadOut
from src.models.account import Account
from src.models.transaction import Transaction
from database import get_session
from security import get_password_hash
from auth_deps import get_current_user
import sqlmodel as sm


router = APIRouter(prefix="/account")

@router.post("/", response_model=AccountOut, status_code=201)
async def create_account(account_data: AccountIn, session: AsyncSession = Depends(get_session)):
    new_account = Account(
        name = account_data.name,
        password=get_password_hash(account_data.password),
        active = account_data.active
    )

    try:
        session.add(new_account)
        await session.commit()
        await session.refresh(new_account)
        return new_account

    except IntegrityError:
        # Erro específico de integridade (ex: violou uma chave única no banco)
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Erro de integridade. Verifique se os dados já existem."
        )
        
    except Exception as e:
        # Qualquer outro erro genérico (banco fora do ar, bug no código)
        await session.rollback()
        # Em produção, logamos o erro 'e' aqui para debugar depois
        print(f"Erro ao criar conta: {e}") 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Erro interno ao criar a conta."
        )

#@router.get("/", response_model=list[AccountOut])
#async def read_all_accounts(session: AsyncSession = Depends(get_session)):
    #query = sm.select(Account)
    #results = await session.exec(query)
    #accounts = results.all()
    #return accounts

@router.get("/", response_model=AccountOut)
async def read_account(current_user: Account = Depends(get_current_user)):
   
    return current_user

@router.post("/transaction", response_model=TransactionReadOut)
async def make_transaction(transaction_data: TransactionCreate, 
                           current_user: Account = Depends(get_current_user),
                           session: AsyncSession = Depends(get_session)):
    new_transaction = Transaction(
        account_id = current_user.id,
        value = transaction_data.value,
        type = transaction_data.type
    )
    
    if new_transaction.value < 0 or new_transaction.value == 0:
            raise HTTPException(status_code=400, detail="Valor inválido.")

    if new_transaction.type == "withdraw":
        
        if new_transaction.value > current_user.balance:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail= "Valor maior do que o saldo disponível"
            ) 
        current_user.balance -= new_transaction.value

    elif new_transaction.type == "deposit":
        current_user.balance += new_transaction.value
    
    else:
        raise HTTPException(status_code=400, detail="Tipo de operação inválido. Use 'withdraw' ou 'deposit'.")
    
    try:
        session.add(new_transaction)
        #Atualiza o estado da conta
        session.add(current_user)
        await session.commit()
        await session.refresh(new_transaction)
        return new_transaction
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao processar transação: {str(e)}")
    
@router.get("/transactions", response_model=list[TransactionReadOut])
async def read_transactions(current_user: Account = Depends(get_current_user), 
                            session: AsyncSession = Depends(get_session)):

    query = (
        sm.select(Transaction)
        .where(Transaction.account_id == current_user.id)
    )
    result = await session.exec(query)
    transactions = result.all()
    if not transactions:
        raise HTTPException(status_code=200, detail="Ainda não foram feitas transações")
        
    return transactions

@router.delete("/", response_model=AccountOut)
async def del_account(current_user: Account = Depends(get_current_user), session: AsyncSession = Depends(get_session)):

    if current_user.balance != 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não é possível encerrar uma conta com saldo diferente de zero. Realize o saque ou depósito total antes."
        )
    
    current_user.active = False

    try:
        session.add(current_user)
        await session.commit()
        await session.refresh(current_user)
        return current_user
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao processar deleção: {str(e)}")
