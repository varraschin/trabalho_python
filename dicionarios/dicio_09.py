# Dicionário para armazenar as notas
notas = {}

# Solicita ao usuário as notas de 4 disciplinas
for i in range(1, 5):
    disciplina = input(f"Digite o nome da {i}ª disciplina: ")
    nota = float(input(f"Digite a nota de {disciplina}: "))
    
    # Armazena a nota no dicionário
    notas[disciplina] = nota

# Calcula a média das notas
media = sum(notas.values()) / len(notas)

# Exibe o dicionário e a média das notas
print("\nNotas por disciplina:")
for disciplina, nota in notas.items():
    print(f"{disciplina}: {nota}")

print(f"\nA média das notas é: {media:.2f}")
