# Solicita o nome do produto
produto = input("Digite o nome do produto: ")

# Solicita a quantidade do produto
quantidade = int(input("Digite a quantidade do produto: "))

# Solicita o preço unitário do produto
preco_unitario = float(input("Digite o preço unitário do produto: R$ "))

# Calcula o valor total da compra
valor_total = quantidade * preco_unitario

# Exibe o resultado
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
