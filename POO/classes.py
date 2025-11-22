class Cachorro:
  def __init__(self, nome, cor, raca, acordado = True):
    self.nome = nome
    self.cor = cor
    self.raca = raca
    self.acordado = acordado

  def latir(self):
    print("Au Au")

  def dormir(self):
    self.acordado = False
    print("Zzzzzz...")

  def __str__(self):  #Descrição da classe
    return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave, valor in self.__dict__.items()]} "

  def __del__(self):  #Este é o método destrutor, serve para realizar alguma operação antes do objeto der destruído.
    print("Destruindo a instância")

cao_1 = Cachorro("James", "Pardo", "Golden Retrivier")
cao_1.latir()

print(cao_1.__str__())