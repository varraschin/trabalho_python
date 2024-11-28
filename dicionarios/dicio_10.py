# Dicionário com informações do livro
livro = {
    "Título": "Dom Casmurro",
    "Autor": "Machado de Assis",
    "Ano de publicação": 1899
}

# Exibe o dicionário original
print("Informações do livro:")
print(livro)

# Solicita ao usuário para atualizar o ano de publicação
novo_ano = int(input("\nDigite o novo ano de publicação: "))

# Atualiza o valor no dicionário
livro["Ano de publicação"] = novo_ano

# Exibe o dicionário atualizado
print("\nInformações do livro atualizadas:")
print(livro)
