class Pessoa:
    # atributos
    nome = "Sicrâno"
    idade = 30
    altura = 1.70

    # método
    def falar(self, texto):# self é um parâmetro obrigatório do python que informa que o método pertence à própria classe que foi criada.
        print (texto)

pessoa1 = Pessoa() #Criando o objeto através da classe
pessoa1.nome = "José"
print(pessoa1.nome, pessoa1.idade)

pessoa1.falar("Hello World")