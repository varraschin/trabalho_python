# Armazena os números de 1 a 20 em uma lista
numeros = list(range(1, 21))

# Exibe apenas os números múltiplos de 3
print("Números múltiplos de 3:")
for numero in numeros:
    if numero % 3 == 0:
        print(numero)
