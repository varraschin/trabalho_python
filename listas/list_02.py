# Solicita ao usuário uma lista de números separados por espaços
entrada = input("Digite uma lista de números separados por espaços: ")

# Converte a entrada em uma lista de números inteiros
numeros = [int(num) for num in entrada.split()]

# Exibe o maior e o menor número da lista
maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
