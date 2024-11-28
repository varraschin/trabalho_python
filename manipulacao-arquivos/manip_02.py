try:
    # Tenta abrir o arquivo mensagem.txt no modo de leitura ('r')
    with open('mensagem.txt', 'r') as arquivo:
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()
        # Exibe o conteúdo na tela
        print(conteudo)
except FileNotFoundError:
    # Caso o arquivo não exista, exibe uma mensagem de erro
    print("Erro: o arquivo 'mensagem.txt' não foi encontrado.")
