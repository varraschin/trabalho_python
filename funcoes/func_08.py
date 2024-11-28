# Definição da função contar_vogais
def contar_vogais(s):
    # Definir as vogais (tanto maiúsculas quanto minúsculas)
    vogais = "aeiouAEIOU"
    # Contar as vogais na string
    contador = 0
    for letra in s:
        if letra in vogais:
            contador += 1
    return contador

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

# Chama a função contar_vogais e armazena o resultado
numero_vogais = contar_vogais(frase)

# Exibe o resultado
print(f"A quantidade de vogais na frase é: {numero_vogais}")
