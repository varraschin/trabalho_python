# Solicita o preço do produto e a porcentagem de desconto
preco = float(input("Digite o preço do produto: R$ "))
desconto_percentual = float(input("Digite a porcentagem de desconto: "))

# Calcula o valor do desconto
valor_desconto = (preco * desconto_percentual) / 100

# Calcula o preço final do produto
preco_final = preco - valor_desconto

# Exibe os resultados
print(f"O valor do desconto é: R$ {valor_desconto:.2f}")
print(f"O preço final do produto com o desconto é: R$ {preco_final:.2f}")
