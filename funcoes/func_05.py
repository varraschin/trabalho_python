# Definição da função media
def media(lista):
    # Calcula a média dividindo a soma dos números pelo número de elementos na lista
    return sum(lista) / len(lista)

# Solicita ao usuário uma lista de números, separando-os por espaço
entrada = input("Digite os números (separados por espaço): ")

# Converte a entrada para uma lista de números inteiros
numeros = [float(num) for num in entrada.split()]

# Chama a função media e armazena o resultado
resultado_media = media(numeros)

# Exibe o resultado
print(f"A média dos números informados é: {resultado_media}")
