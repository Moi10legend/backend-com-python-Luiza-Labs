#Um iterador é um objeto que contém um número contável de valores que
#podem ser iterados, ou seja, que pode percorrer todos os valrores.
#O protocolo do iterador é uma maneira do python fazer a iteração de 
#um objeto que consiste em dois métodos especiais: "__iter__()" e "__next__()"

class Meuiterador:
    def __init__(self, numeros):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
    
for i in Meuiterador(numeros=[1, 2, 3, 4, 5, 6, 7]):
    print(i)