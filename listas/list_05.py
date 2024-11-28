# Solicita ao usuário uma lista de números inteiros separados por espaços
entrada = input("Digite uma lista de números inteiros separados por espaços: ")

# Converte a entrada em uma lista de números inteiros
numeros = [int(num) for num in entrada.split()]

# Calcula a soma de todos os números da lista
soma = sum(numeros)

# Exibe o resultado
print(f"A soma de todos os números é: {soma}")
