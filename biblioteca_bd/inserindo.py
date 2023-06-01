import pymysql

conexao = pymysql.connect(
    host ="localhost",
    user ="root",
    password ="",
    database="biblioteca_bd"
)

cod_livro = int(input("Informe o código do livro: "))
titulo = (input("Informe o titulo do livro: "))
autor = (input("Informe o autor do livro: "))
ano_publicacao = int(input("Informe o ano de publicação: "))

comando = "insert into livros values(%s, %s, %s, %s)"

campos = (cod_livro, titulo, autor, ano_publicacao)

consulta = conexao.cursor()

consulta.execute(comando, campos)

conexao.commit()

print(consulta.rowcount,"linha(s) inserida com sucesso\n")

conexao.close()
