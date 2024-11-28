# Solicita a primeira lista de 5 números
lista1 = []
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número da primeira lista: "))
    lista1.append(numero)

# Solicita a segunda lista de 5 números
lista2 = []
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número da segunda lista: "))
    lista2.append(numero)

# Cria uma nova lista com a soma dos elementos correspondentes
soma_listas = [lista1[i] + lista2[i] for i in range(5)]

# Exibe a nova lista
print(f"A nova lista com a soma dos elementos correspondentes é: {soma_listas}")
