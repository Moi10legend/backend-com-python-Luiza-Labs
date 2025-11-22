class Animal:
    def __init__(self, numero_patas, numero_olhos):
        self.numero_patas = numero_patas
        self.numero_olhos = numero_olhos

    def __str__(self):  #Descrição da classe
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])} "

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    def __init__(self, **kw):
        super().__init__(**kw)

class Ornitorrinco(Ave, Mamifero):
    pass

ornitorrinco = Ornitorrinco(numero_patas=4, numero_olhos=2, cor_bico="marrom", cor_pelo="marrom")

print(ornitorrinco)
