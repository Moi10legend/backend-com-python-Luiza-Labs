#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print(f"Adição: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")

if numero2 != 0:
    print(f"Divisão: {numero1 / numero2}")
else:
    print("Divisão: Erro - divisão por zero não permitida")
