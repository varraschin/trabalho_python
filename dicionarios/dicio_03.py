# Cria um dicionário vazio para armazenar as informações do produto
produto = {}

# Solicita ao usuário o nome, preço e quantidade do produto
produto['nome'] = input("Digite o nome do produto: ")
produto['preco'] = float(input("Digite o preço do produto: R$ "))
produto['quantidade'] = int(input("Digite a quantidade em estoque do produto: "))

# Exibe o dicionário completo
print("\nInformações do produto:")
print(produto)
