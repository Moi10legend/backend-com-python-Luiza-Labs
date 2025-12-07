#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar
numero = int(input("Digite um número inteiro: "))
resultado = "par" if numero % 2 == 0 else "ímpar"
print(f"O número {numero} é {resultado}.")
