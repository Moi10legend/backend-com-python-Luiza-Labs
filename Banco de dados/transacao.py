import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
con = sqlite3.connect(ROOT_PATH / "meu_banco.db") #Criando um banco de dados/acessando banco de dados
cursor = con.cursor()

try:
    cursor.execute("DELETE FROM Clientes WHERE email=2")
    con.commit()
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES(?, ?)", ("Teste", 2))
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES(?, ?, ?)", (2, "Teste", 2))
    con.commit()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    con.rollback()  #Se houver algum erro na tentativa da transação, o estado do banco de dados volta para o anterior
