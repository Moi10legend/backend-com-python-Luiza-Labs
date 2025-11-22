#Introspecção é a capacidade da função de entender seus argumentos em tempo de execução

import functools

def meu_decorador4(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes")
        funcao(*args, **kwargs)
        print("Faz algo depois")

    return envelope

@meu_decorador4
def boas_vindas(nome):
    print(f"Olá {nome}, seja bem-vindo!")

print(boas_vindas.__name__)