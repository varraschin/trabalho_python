# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Dicionário para armazenar a frequência de cada letra
frequencia = {}

# Conta a frequência de cada letra na palavra
for letra in palavra:
    # Se a letra já está no dicionário, incrementa o contador
    if letra in frequencia:
        frequencia[letra] += 1
    # Caso contrário, adiciona a letra no dicionário com valor 1
    else:
        frequencia[letra] = 1

# Exibe o dicionário com a frequência das letras
print("Frequência de cada letra na palavra:")
print(frequencia)
