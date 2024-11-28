# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 5 números ao usuário e os armazena na lista
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

# Encontra o maior número na lista
maior_numero = max(numeros)

# Substitui o maior número por 0
indice_maior = numeros.index(maior_numero)
numeros[indice_maior] = 0

# Exibe a lista atualizada
print(f"A lista atualizada é: {numeros}")
