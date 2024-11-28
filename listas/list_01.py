# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 5 números ao usuário e os armazena na lista
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

# Exibe a lista completa
print("A lista completa dos números é:", numeros)
