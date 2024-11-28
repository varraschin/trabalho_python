# Definição da função fatorial
def fatorial(n):
    # Verifica se o número é negativo
    if n < 0:
        return "Fatorial não definido para números negativos"
    
    # Inicializa o resultado do fatorial como 1
    resultado = 1
    
    # Calcula o fatorial usando um loop
    for i in range(1, n + 1):
        resultado *= i  # Multiplica o resultado pelo número i
    
    return resultado

# Solicita ao usuário um número
numero_usuario = int(input("Digite um número para calcular o fatorial: "))

# Chama a função fatorial e armazena o resultado
resultado_fatorial = fatorial(numero_usuario)

# Exibe o resultado
print(f"O fatorial de {numero_usuario} é {resultado_fatorial}.")
