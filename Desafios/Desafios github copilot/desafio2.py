#vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.
string: str = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
resultado = " ".join([string] * numero)
print("Resultado da repetição:", resultado)