# Definição da função soma
def soma(num1, num2):
    return num1 + num2

# Solicita dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chama a função soma e armazena o resultado
resultado = soma(numero1, numero2)

# Exibe o resultado
print(f"A soma de {numero1} e {numero2} é {resultado}.")
