# Solicita três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Troca os valores conforme a descrição
numero1, numero2, numero3 = numero2, numero3, numero1

# Exibe os novos valores das variáveis
print(f"Novo valor do primeiro número: {numero1}")
print(f"Novo valor do segundo número: {numero2}")
print(f"Novo valor do terceiro número: {numero3}")
