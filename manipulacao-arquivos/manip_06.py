# Solicita ao usuário o nome do arquivo e o texto a ser gravado
nome_arquivo = input("Digite o nome do arquivo (com a extensão .txt): ")
texto = input("Digite o texto a ser gravado no arquivo: ")

try:
    # Abre o arquivo no modo de escrita ('w'). Se o arquivo não existir, ele será criado.
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve o texto no arquivo
        arquivo.write(texto)
    
    print(f'O texto foi gravado com sucesso no arquivo {nome_arquivo}')

except Exception as e:
    # Caso ocorra algum erro, exibe uma mensagem
    print(f"Erro ao criar ou gravar o arquivo: {e}")
