# Definição da função inverter
def inverter(s):
    # Retorna a string invertida usando slicing
    return s[::-1]

# Solicita ao usuário uma palavra
palavra = input("Digite uma palavra: ")

# Chama a função inverter e armazena o resultado
resultado_invertido = inverter(palavra)

# Exibe o resultado
print(f"A palavra invertida é: {resultado_invertido}")
