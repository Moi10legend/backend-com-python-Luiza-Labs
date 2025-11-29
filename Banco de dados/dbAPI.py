import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
con = sqlite3.connect(ROOT_PATH / "meu_banco.db") #Criando um banco de dados/acessando banco de dados
cursor = con.cursor()

#Criando uma tabela
#cursor.execute("CREATE TABLE Clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

#Inserindo dados em uma tabela

# nome = "Moisés"
# email = "m10@gmail.com"

# cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?);", (nome, email))
# con.commit()

# data = ("Giovan", "g30@gmail.com")
# cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?);", data)
#É necessário commitar sobre uma operação feita no banco de dados
#con.commit()

#Atualizando um dado na tabela
# data = ("Çica", 2)
# cursor.execute("UPDATE Clientes SET nome = ? WHERE id = ?", data)
# con.commit()

#Deletando um registro
# data = (1,)
# cursor.execute("DELETE FROM Clientes WHERE id=?", (3,))
# con.commit()

#Inserindo registros em lote
# data = [("Galvão Bueno", "galvao@gmail.com"), ("Cristiano Ronaldo", "cris@gmail.com"), ("Júlia Rabelo", "rabelo@gmail.com")]
# cursor.executemany("INSERT INTO Clientes (nome, email) VALUES (?, ?);", data)
# con.commit()

#Fazendo uma consulta ao banco, retornando apenas 1 registro
cursor.execute("SELECT * FROM Clientes WHERE id=2") 
result = cursor.fetchone()
print(result)  

#Fazendo uma consulta retornando todos os registros
cursor.row_factory = sqlite3.Row
cursor.execute("SELECT * FROM Clientes ORDER BY nome") #Está ordenando a consulta pelos nomes
results = cursor.fetchall()
for row in results:
    print(dict(row)) #Transforma o retorno em um dicionário de chave(nome do campo) e valor,
