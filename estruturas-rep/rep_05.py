# Inicializa a variável para armazenar a soma
soma = 0

# Usa um loop para pedir 5 números ao usuário e somá-los
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    soma += numero  # Adiciona o número à soma

# Exibe o resultado
print(f"A soma dos números é: {soma}")
