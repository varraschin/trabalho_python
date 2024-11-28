# Cria uma lista vazia para armazenar os nomes
nomes = []

# Solicita 5 nomes ao usuário e os armazena na lista
for i in range(1, 6):
    nome = input(f"Digite o {i}º nome: ")
    nomes.append(nome)

# Exibe os nomes na ordem inversa
print("Nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
