# Definição da função é_bissexto
def é_bissexto(ano):
    # Um ano é bissexto se for divisível por 4, mas não por 100, ou se for divisível por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicita ao usuário o ano
ano = int(input("Digite um ano: "))

# Chama a função é_bissexto e armazena o resultado
resultado = é_bissexto(ano)

# Exibe o resultado
if resultado:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
