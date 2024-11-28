# Cria um dicionário vazio para armazenar os dados dos alunos
alunos = {}

# Solicita o nome e a nota de 5 alunos
for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

# Exibe o nome e a nota de cada aluno
print("\nNotas dos alunos:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")
