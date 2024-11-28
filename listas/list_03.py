# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 10 números ao usuário e os armazena na lista
for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

# Exibe os números pares da lista
print("Números pares na lista:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
