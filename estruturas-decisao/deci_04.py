# Solicita uma nota de 0 a 10
nota = float(input("Digite uma nota de 0 a 10: "))

# Verifica se a nota está no intervalo válido
if 0 <= nota <= 10:
    print("Nota válida.")
else:
    print("Erro! A nota deve estar no intervalo de 0 a 10.")
