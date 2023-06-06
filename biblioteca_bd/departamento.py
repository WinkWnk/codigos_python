import pymysql

class Departamento:
    
    def conexao(self):
        con= pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="biblioteca_bd"
        )
        
        return con

    def inserir(self, cod_livro, titulo, autor, ano_publicacao):
        conexao= self.conexao() #está chamando o método que irá logar no banco
        
        comando = "insert into livros values(%s, %s, %s,%s )"
        
        campos = (cod_livro, titulo, autor, ano_publicacao)
        consulta = conexao.cursor()
        consulta.execute(comando, campos)
        conexao.commit()
        
        print(consulta.rowcount, "linha inserida com sucesso\n")
        conexao.close()

    def atualizarTitulo(self, titulo, cod_livro):
        conexao = self.conexao()
        self.tirulo = titulo
        self.cod_livro = cod_livro
        
        comando = "update livros set titulo = %s where cod_livro = %s"
        valores = (self.titulo, self.cod_livro)

        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        print("Linha atualizada com sucesso!\n ")
        conexao.close()















'''
        def consultar(self):
        conexao= self.conexao()
        
        comando= "select * from livros"
        consulta= conexao.cursor()
        consulta.execute(comando)
        
        resultado= consulta.fetchall()
        
        print(resultado, "\n")
        
        conexao.close()
'''