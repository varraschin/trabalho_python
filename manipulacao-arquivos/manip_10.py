def adicionar_entrada():
    # Solicita a entrada do usuário
    entrada = input("Digite sua nova entrada para o diário: ")

    try:
        # Abre o arquivo em modo 'append' para adicionar no final (ou cria se não existir)
        with open('diario.txt', mode='a') as arquivo:
            arquivo.write(entrada + '\n')  # Adiciona a entrada no arquivo, seguida de uma nova linha

        print("Entrada adicionada com sucesso ao diário!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chama a função para adicionar a entrada
adicionar_entrada()
