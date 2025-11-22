def meu_decorador2(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes")
        funcao(*args, **kwargs)
        print("Faz algo depois")

    return envelope

@meu_decorador2
def boas_vindas(nome):
    print(f"Olá {nome}, seja bem-vindo!")

boas_vindas("Mika haikkonen")
