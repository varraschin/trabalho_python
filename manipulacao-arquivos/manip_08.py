try:
    # Abre o arquivo original.txt no modo de leitura ('r')
    with open('original.txt', 'r') as arquivo_original:
        # Lê o conteúdo do arquivo original
        conteudo = arquivo_original.read()
    
    # Abre o arquivo copia.txt no modo de escrita ('w')
    with open('copia.txt', 'w') as arquivo_copia:
        # Escreve o conteúdo do arquivo original no arquivo de cópia
        arquivo_copia.write(conteudo)
    
    print("Conteúdo copiado com sucesso de 'original.txt' para 'copia.txt'.")

except FileNotFoundError:
    # Caso o arquivo original não seja encontrado, exibe uma mensagem de erro
    print("Erro: o arquivo 'original.txt' não foi encontrado.")
except Exception as e:
    # Caso ocorra algum outro erro, exibe uma mensagem com o erro
    print(f"Ocorreu um erro: {e}")
