class Iterador_de_arquivo:
    def __init__(self, arquivo):
        self.arquivo = open(arquivo)

    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.arquivo.readline()
        if line != "":
            return line
        else:
            self.arquivo.close()
            raise StopIteration
        
for line in Iterador_de_arquivo('Assessor.txt'):
    print(line)