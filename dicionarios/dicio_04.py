# Dicionário previamente definido com nomes de pessoas
pessoas = {
    "João": 25,
    "Maria": 30,
    "Carlos": 22,
    "Ana": 28,
    "Pedro": 35
}

# Solicita o nome da pessoa ao usuário
nome_usuario = input("Digite o nome de uma pessoa: ")

# Verifica se o nome está presente no dicionário
if nome_usuario in pessoas:
    print(f"O nome {nome_usuario} foi encontrado no dicionário.")
else:
    print(f"O nome {nome_usuario} não foi encontrado no dicionário.")
