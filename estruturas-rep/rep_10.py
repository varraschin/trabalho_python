# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é válido
if numero <= 1:
    print("Erro! O número deve ser maior que 1.")
else:
    # Variável para verificar se é primo
    is_primo = True
    
    # Loop para verificar se o número tem divisores além de 1 e ele mesmo
    for i in range(2, numero):
        if numero % i == 0:  # Se o número for divisível por algum outro número
            is_primo = False
            break
    
    # Exibe se o número é primo ou não
    if is_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
