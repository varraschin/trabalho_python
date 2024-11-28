# Dicionário que mapeia números (1 a 7) para os dias da semana
dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

# Solicita ao usuário um número entre 1 e 7
numero = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))

# Verifica se o número está no intervalo válido
if 1 <= numero <= 7:
    # Exibe o dia da semana correspondente ao número
    print(f"O dia da semana correspondente ao número {numero} é {dias_da_semana[numero]}.")
else:
    # Mensagem de erro caso o número não esteja no intervalo de 1 a 7
    print("Número inválido. Por favor, digite um número de 1 a 7.")
