# Dicionário com preços de 5 produtos
produtos = {
    "Arroz": 20.50,
    "Feijão": 15.30,
    "Macarrão": 8.40,
    "Açúcar": 5.20,
    "Óleo": 6.99
}

# Solicita o nome do produto ao usuário
produto_usuario = input("Digite o nome do produto para saber o preço: ")

# Verifica se o produto está no dicionário
if produto_usuario in produtos:
    # Exibe o preço do produto
    print(f"O preço do {produto_usuario} é R$ {produtos[produto_usuario]:.2f}.")
else:
    # Exibe mensagem de erro se o produto não for encontrado
    print(f"O produto '{produto_usuario}' não foi encontrado.")
