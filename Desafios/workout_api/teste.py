fake_db = [{"Id": 123, 
            "Nome": "Mohamed Ali", 
            "CPF": "123.456.789-09", 
            "Idade": 45, 
            "Peso": 87, 
            "Altura": 1.89,
            "Sexo": "M",
            "Centro de treinamento": 1,
            "Categoria": 1}]

def read_all():
    atletas = []
    for atleta in fake_db:
        atleta_novo = {"Nome": atleta["Nome"], 
                       "Centro de treinamento": atleta["Centro de treinamento"], 
                       "Categoria": atleta["Categoria"]}
        atletas.append(atleta_novo)
    print(atletas)

read_all()