# Abre o arquivo dados.txt no modo escrita ('w')
with open('dados.txt', 'w') as arquivo:
    # Escreve a frase no arquivo
    arquivo.write("Este é o meu primeiro arquivo em Python!")

print("Arquivo criado e frase escrita com sucesso!")
