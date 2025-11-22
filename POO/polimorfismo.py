class Passaro:
    def voar(self):
        print("Voando")

class Canarinho(Passaro):
    def voar(self):
        super().voar()
    
class Pinguim:
    def voar(self):
        print("Pinguim não voa")

def plano_de_voo(passaro):
    passaro.voar()

pinguim = Pinguim()
canarinho = Canarinho()

plano_de_voo(pinguim)
plano_de_voo(canarinho)