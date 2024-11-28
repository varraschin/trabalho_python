# Solicita a distância percorrida (em km) e o tempo gasto (em horas)
distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

# Calcula a velocidade média
velocidade_media = distancia / tempo

# Exibe o resultado
print(f"A velocidade média foi de {velocidade_media:.2f} km/h.")
