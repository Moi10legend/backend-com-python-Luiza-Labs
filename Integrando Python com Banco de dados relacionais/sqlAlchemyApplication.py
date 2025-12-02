from sqlalchemy.orm import declarative_base, relationship, Session
import sqlalchemy as sqlA

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atibrutos
    id = sqlA.Column(sqlA.Integer, primary_key = True)
    name = sqlA.Column(sqlA.String(20), nullable=False)
    email = sqlA.Column(sqlA.String(50), nullable=False)

    #define a relação com a tabela Address
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    #Retorna a representação da tabela, como se fosse o método __str__
    def __repr__(self):
        return f"User (id={self.id}, name={self.name}, email={self.email})"


class Address(Base):
    __tablename__ = "address"
    id = sqlA.Column(sqlA.Integer, primary_key=True, autoincrement=True)
    rua = sqlA.Column(sqlA.String(50))
    bairro = sqlA.Column(sqlA.String(40))
    cidade = sqlA.Column(sqlA.String(40))
    estado = sqlA.Column(sqlA.String(19))
    user_id = sqlA.Column(sqlA.Integer, sqlA.ForeignKey("user_account.id"), nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address (id={self.id}, rua={self.rua}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado})"
    
print(User.__tablename__)
print(Address.__tablename__)

#Criação da engine
engine = sqlA.create_engine("sqlite://")

Base.metadata.create_all(engine)

#Criação do inspetor
insp = sqlA.inspect(engine)

print(insp.has_table("user_account"))
print(insp.get_table_names())
print(insp.default_schema_name)

with Session(engine) as session:
    juliana = User(
        name="Juliana",
        email="juli@gmail.com",
        address=[Address(rua="Hélio Brandão", bairro="Ipsep", cidade="Recife", estado="Pernambuco")]
    )

    francine = User(
        name="Francine",
        email="fran@gmail.com",
        address=[Address(rua="Avenida Jean-Emily favile", bairro="Ipsep", cidade="Recife", estado="Pernambuco"),
                 Address(rua="Avenida Doutor José Rufino", bairro="Barro", cidade="Recife", estado="Pernambuco")]
    )

    #enviando para o db (persistência de dados)
    session.add_all([juliana, francine])
    session.commit()

#Fazendo a consulta ao BD
stmt = sqlA.select(User).where(User.name.in_(["Juliana"]))

for user in session.scalars(stmt):
    print(user)

stmt_address = sqlA.select(Address).where(Address.user_id.in_([1]))
for address in session.scalars(stmt_address):
    print(address)

print("\nRecuperando info ordenada")
order_stmt = sqlA.select(User).order_by(User.name.desc())
for result in session.scalars(order_stmt):
    print(result)

join_stmt = sqlA.select(User.name, Address).join_from(Address, User)
# for result in session.scalars(join_stmt):
#     print(result)
print(join_stmt)

connection = engine.connect()
results = connection.execute(join_stmt).fetchall()
print("\nExecutando statement a partir da conncetion")
for result in results:
    print(result)

#Contando o número de instâncias/registros da tabela Users
stmt_count = sqlA.select(sqlA.func.count("*")).select_from(User)
# for result in session.scalars(stmt_count):
#     print(result)