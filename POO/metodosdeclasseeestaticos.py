class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, nome, dia, mes, ano):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def eh_maior_de_idade(idade):
        if idade >= 18:
            print("É maior de idade")
        else:
            print("É menor de idade")
    
p = Pessoa.criar_de_data_nascimento("Alfredo", 2, 3, 2006)
p.eh_maior_de_idade(18)
Pessoa.eh_maior_de_idade(2)
print(p.nome, p.idade)
