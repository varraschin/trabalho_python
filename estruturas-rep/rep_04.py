# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero >= 0:
    # Inicializa a variável para o fatorial
    fatorial = 1
    
    # Usa um loop para calcular o fatorial
    for i in range(1, numero + 1):
        fatorial *= i  # Multiplica fatorial pelo número atual
    
    # Exibe o resultado
    print(f"O fatorial de {numero} é: {fatorial}")
else:
    print("Erro! Por favor, digite um número inteiro positivo.")
