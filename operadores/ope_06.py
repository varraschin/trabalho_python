# Solicita dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Troca os valores usando operadores matemáticos
numero1 = numero1 + numero2  # Soma os dois números
numero2 = numero1 - numero2  # Subtrai o número2 do total, restituindo o valor original de numero1
numero1 = numero1 - numero2  # Subtrai o novo numero2 do total, restituindo o valor original de numero2

# Exibe os valores trocados
print(f"Após a troca: \nPrimeiro número: {numero1} \nSegundo número: {numero2}")
