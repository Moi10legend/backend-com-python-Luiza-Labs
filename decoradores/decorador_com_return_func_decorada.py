def meu_decorador3(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois")
        return resultado

    return envelope

@meu_decorador3
def boas_vindas(nome):
    print(f"Olá {nome}, seja bem-vindo!")
    return nome.upper()

boas_vindas("Mika haikkonen")
print(boas_vindas("Mika haikkonen"))
