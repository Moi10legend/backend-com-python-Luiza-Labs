from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    
    def ligar(self):
        print("Tv Ligada")

    def desligar(self):
        print("Tv desligada")

    @property
    def marca(self):
        return "Philco"

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)