# Solicita ao usuário uma lista de palavras, separadas por espaços
entrada = input("Digite uma lista de palavras separadas por espaços: ")

# Converte a entrada em uma lista de palavras
palavras = entrada.split()

# Solicita ao usuário uma palavra específica para buscar
palavra_buscar = input("Digite a palavra que deseja buscar: ")

# Verifica se a palavra está na lista
if palavra_buscar in palavras:
    print(f"A palavra '{palavra_buscar}' está presente na lista.")
else:
    print(f"A palavra '{palavra_buscar}' não está presente na lista.")
