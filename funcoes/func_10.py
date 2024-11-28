# Definição da função tabuada
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicita ao usuário um número
numero = int(input("Digite um número para ver a sua tabuada: "))

# Chama a função tabuada com o número fornecido pelo usuário
tabuada(numero)
