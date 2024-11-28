import math

# Solicita um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o dobro, o triplo e a raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = math.sqrt(numero)

# Exibe os resultados
print(f"O dobro de {numero} é {dobro}.")
print(f"O triplo de {numero} é {triplo}.")
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")
