class Estudante:
    escola = "DIO"  #Variável de classe

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero} - {self.escola})"
    
e1 = Estudante("Fabricio", 20394)
e2 = Estudante("Emanuela", 10194)

print(e1.__str__())
print(e2.__str__())