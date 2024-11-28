try:
    # Abre o arquivo numeros.txt no modo de leitura ('r')
    with open('numeros.txt', 'r') as arquivo:
        # Inicializa uma variável para armazenar a soma
        soma = 0
        
        # Lê cada linha do arquivo
        for linha in arquivo:
            # Converte a linha para um número inteiro e soma ao total
            soma += int(linha.strip())  # strip() remove espaços em branco e quebras de linha
            
    # Exibe o resultado da soma
    print(f'A soma dos números no arquivo é: {soma}')

except FileNotFoundError:
    # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
    print("Erro: o arquivo 'numeros.txt' não foi encontrado.")
except ValueError:
    # Caso ocorra um erro ao tentar converter o conteúdo para inteiro, exibe uma mensagem de erro
    print("Erro: o arquivo contém valores inválidos (não numéricos).")
