# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero > 0:
    # Exibe todos os números de 1 até o número informado
    for i in range(1, numero + 1):
        print(i)
else:
    print("Erro! Por favor, digite um número inteiro positivo.")
