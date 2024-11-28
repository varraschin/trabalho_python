# Solicita os dois números inteiros positivos ao usuário
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Verifica se o início é maior que o fim
if inicio > fim:
    print("Erro! O início não pode ser maior que o fim.")
else:
    # Exibe os números pares no intervalo
    print(f"Números pares entre {inicio} e {fim}:")
    for numero in range(inicio, fim + 1):  # Percorre o intervalo
        if numero % 2 == 0:  # Verifica se o número é par
            print(numero)
