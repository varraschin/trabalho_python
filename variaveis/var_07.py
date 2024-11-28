# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a mensagem com o nome e a média
print(f"{nome}, sua média é {media:.2f}.")
