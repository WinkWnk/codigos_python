class Pessoa: #superclasse ou classe mãe
    def __init__(self, nome, idade):
        self._nome = nome # Ao utilizar apenas 1 underline, dizemos que o atributo está com o modificador protegido, ou seja, as classes filhas tem acesso aos atributos da classe mãe.
        self._idade = idade

    def relatorio(self):
        print("Sou uma pessoa.""\n")
        print(f"Olá {self._nome}, sua idade é {self._idade}\n")

class Aluno(Pessoa):
    def mostraAluno(self):
        print(f"Sou aluno e meu nome é {self._nome}\n")
        
class Professor(Pessoa):
    def mostraProfessor(self):
        print(f"Sou professor de física e meu nome é {self._nome}\n")