# Cria um dicionário vazio para armazenar os pares chave-valor
dados = {}

# Solicita ao usuário 3 pares de chave e valor
for i in range(1, 4):
    chave = input(f"Digite a chave para o {i}º par (por exemplo, nome): ")
    valor = input(f"Digite o valor para a chave '{chave}': ")
    
    # Armazena o par chave-valor no dicionário
    dados[chave] = valor

# Exibe o dicionário completo
print("\nDicionário completo:")
print(dados)
