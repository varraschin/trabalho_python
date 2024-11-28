# Definição da função maior
def maior(num1, num2, num3):
    # Retorna o maior número usando a função max()
    return max(num1, num2, num3)

# Solicita ao usuário três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chama a função maior e armazena o resultado
resultado_maior = maior(numero1, numero2, numero3)

# Exibe o resultado
print(f"O maior número entre {numero1}, {numero2} e {numero3} é {resultado_maior}.")
