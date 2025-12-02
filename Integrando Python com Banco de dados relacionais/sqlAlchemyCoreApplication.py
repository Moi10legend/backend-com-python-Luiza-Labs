import sqlalchemy as sqlA

engine = sqlA.create_engine("sqlite:///:memory")

metadata_obj = sqlA.MetaData()
user = sqlA.Table(
    "user",
    metadata_obj,
    sqlA.Column("user_id", sqlA.Integer, primary_key=True, autoincrement=True),
    sqlA.Column("name", sqlA.String(20), nullable=False),
    sqlA.Column("email_addres", sqlA.String(60)),
    sqlA.Column("nickname", sqlA.String(20), nullable=False)
)

user_prefs = sqlA.Table(
    "user_prefs", metadata_obj,
    sqlA.Column("pref_id", sqlA.Integer, primary_key=True),
    sqlA.Column("user_id", sqlA.Integer, sqlA.ForeignKey("user.user_id"), nullable=False),
    sqlA.Column("pref_name", sqlA.String(40), nullable=False),
    sqlA.Column("pref_value", sqlA.String(100))
)

#Retorna as tabelas do BD
for table in metadata_obj.sorted_tables:
    print(table)

#Retornando informações da tabela
print(user.primary_key)

metadata_obj.create_all(engine)

#Utilizando o SQL na consulta e transação
with engine.connect() as connection:
    # with connection.begin():
    #     connection.execute(sqlA.text("INSERT INTO user VALUES(1,'Pablo', 'pablo@gmail.com', 'pablito')"))
    
    result = connection.execute(sqlA.text("SELECT * FROM user"))
    for row in result:
        print(row)