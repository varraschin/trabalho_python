try:
    # Abre o arquivo texto.txt no modo de leitura ('r')
    with open('texto.txt', 'r') as arquivo:
        # Inicializa o contador de palavras
        total_palavras = 0
        
        # Lê o conteúdo do arquivo linha por linha
        for linha in arquivo:
            # Divide a linha em palavras usando o método split(), que separa por espaços em branco
            palavras = linha.split()
            
            # Atualiza o contador com o número de palavras na linha
            total_palavras += len(palavras)
    
    # Exibe o total de palavras
    print(f'O total de palavras no arquivo é: {total_palavras}')

except FileNotFoundError:
    # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
    print("Erro: o arquivo 'texto.txt' não foi encontrado.")
