# Inicializa a variável para armazenar a soma
soma = 0

# Loop para solicitar números ao usuário até que ele digite 0
while True:
    numero = int(input("Digite um número (digite 0 para parar): "))
    
    # Verifica se o número é 0, caso em que o loop é interrompido
    if numero == 0:
        break
    
    # Soma o número à variável soma
    soma += numero

# Exibe a soma total dos números
print(f"A soma de todos os números digitados é: {soma}")
