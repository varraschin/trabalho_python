# Solicita dois números e um operador matemático ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Realiza a operação correspondente
if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado de {numero1} + {numero2} é: {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado de {numero1} - {numero2} é: {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"O resultado de {numero1} * {numero2} é: {resultado}")
elif operador == "/":
    if numero2 != 0:  # Verifica se o divisor é zero
        resultado = numero1 / numero2
        print(f"O resultado de {numero1} / {numero2} é: {resultado}")
    else:
        print("Erro! Não é possível dividir por zero.")
else:
    print("Operador inválido! Por favor, escolha um operador válido (+, -, *, /).")
