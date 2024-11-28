# Definição da função calcular_preco_final
def calcular_preco_final(preco, desconto):
    # Calcula o valor do desconto
    valor_desconto = preco * (desconto / 100)
    # Calcula o preço final
    preco_final = preco - valor_desconto
    return preco_final

# Solicita ao usuário o preço do produto
preco_produto = float(input("Digite o preço do produto: R$ "))

# Solicita ao usuário a porcentagem de desconto
desconto = float(input("Digite a porcentagem de desconto: "))

# Chama a função calcular_preco_final e armazena o resultado
preco_final = calcular_preco_final(preco_produto, desconto)

# Exibe o preço final
print(f"O preço final do produto com {desconto}% de desconto é: R$ {preco_final:.2f}")
