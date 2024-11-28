try:
    # Abre o arquivo 'alunos.txt' no modo de leitura ('r')
    with open('alunos.txt', 'r') as arquivo:
        # Lê o conteúdo do arquivo linha por linha
        for linha in arquivo:
            # Remove espaços em branco e quebras de linha ao redor do nome
            nome = linha.strip()
            
            # Verifica se o nome começa com a letra "A"
            if nome.lower().startswith('a'):
                # Exibe o nome
                print(nome)
                
except FileNotFoundError:
    # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
    print("Erro: o arquivo 'alunos.txt' não foi encontrado.")
