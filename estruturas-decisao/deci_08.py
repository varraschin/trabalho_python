# Solicita três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Verifica se todos os números são iguais
if numero1 == numero2 == numero3:
    print("Os três números são iguais.")
else:
    # Encontra o maior número
    maior = max(numero1, numero2, numero3)
    print(f"O maior número é: {maior}")
