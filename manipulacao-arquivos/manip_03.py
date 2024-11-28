# Solicita o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Abre o arquivo usuario.txt no modo de acréscimo ('a')
with open('usuario.txt', 'a') as arquivo:
    # Escreve as informações no arquivo, separando nome e idade por vírgula
    arquivo.write(f"{nome}, {idade}\n")

print("Dados adicionados ao arquivo com sucesso!")
    