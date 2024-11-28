import csv

try:
    # Abre o arquivo CSV em modo de leitura
    with open('dados.csv', mode='r') as arquivo_csv:
        # Cria um leitor CSV
        leitor = csv.reader(arquivo_csv)

        # Exibe os dados em formato tabular
        for linha in leitor:
            print("\t".join(linha))  # Junta os valores de cada linha com tabulação para formatar a tabela

except FileNotFoundError:
    print("Erro: o arquivo 'dados.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
