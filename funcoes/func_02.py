# Definição da função é_par
def é_par(numero):
    # Verifica se o número é divisível por 2
    if numero % 2 == 0:
        return True
    else:
        return False

# Solicita ao usuário um número
numero_usuario = int(input("Digite um número para verificar se é par: "))

# Chama a função é_par e armazena o resultado
resultado = é_par(numero_usuario)

# Exibe o resultado
if resultado:
    print(f"O número {numero_usuario} é par.")
else:
    print(f"O número {numero_usuario} não é par (é ímpar).")
