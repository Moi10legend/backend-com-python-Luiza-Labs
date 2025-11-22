class Veiculo:
    def __init__(self, cor, placa, qntd_rodas):
        self.cor = cor
        self.placa = placa
        self.qntd_rodas = qntd_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):  #Descrição da classe
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])} "


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):
    def __init__(self, cor, placa, qntd_rodas, carregado):
        super().__init__(cor, placa, qntd_rodas)
        self.carregado = carregado

    def estah_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")

moto = Motocicleta("Prata", "EQL-1345", 2)
moto.ligar_motor()

caminhao = Caminhão("Vermelho", "YTD-0965", 8, True)
caminhao.estah_carregado()
print(caminhao)