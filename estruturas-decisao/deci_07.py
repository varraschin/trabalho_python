# Solicita o peso e a altura ao usuário
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC e exibe a mensagem correspondente
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print(f"Seu IMC é {imc:.2f}. Você está com peso normal.")
else:
    print(f"Seu IMC é {imc:.2f}. Você está acima do peso.")
