#Vamos testar se uma palavra é um palíndromo
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")