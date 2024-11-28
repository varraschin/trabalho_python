# Solicita o valor do salário bruto
salario_bruto = float(input("Digite o valor do salário bruto: R$ "))

# Solicita o valor do desconto
desconto = float(input("Digite o valor do desconto: R$ "))

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto

# Exibe o resultado
print(f"O salário líquido é: R$ {salario_liquido:.2f}")
