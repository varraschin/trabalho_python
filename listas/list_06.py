# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 10 números ao usuário e os armazena na lista
for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

# Calcula a média dos números na lista
media = sum(numeros) / len(numeros)

# Conta a quantidade de números maiores que a média
contagem_maiores_que_media = sum(1 for numero in numeros if numero > media)

# Exibe o resultado
print(f"A média da lista é: {media}")
print(f"A quantidade de números maiores que a média é: {contagem_maiores_que_media}")
