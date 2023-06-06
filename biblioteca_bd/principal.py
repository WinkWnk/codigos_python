from departamento import Departamento

f1 = Departamento()

print("BOAS VINDAS Á BIBLIOTECA FILADELFIA!!!")
print("===================<>===================\n")

    insert = input("O que você deseja fazer? |1 - Inserir|, |2 - Atualizar|, |3 - Consultar|, |4 - Deletar|, |5 - Sair|: ")

    if insert == 1:
        cod_livro = int(input("Informe o código do livro: "))
        titulo = input("Informe o titulo do livro: ")
        autor = input("Informe o autor do livro: ")
        ano_publicacao = int(input("Informe o ano de publicação: "))
        f1.inserir(cod_livro, titulo, autor, ano_publicacao)

    elif insert == 2:
        titulo = input("Digite o título a ser atualizado: ")
        cod_livro = input("Digite o código referente ao livro: ")
        f1.atualizarTitulo(titulo, cod_livro):
        