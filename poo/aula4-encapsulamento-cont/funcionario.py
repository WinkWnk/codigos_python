class Funcionario:
    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo

    #PRIMEIRA FORMA DE USAR O GET E O SET.

    def getNome(self):
        return self.__nome
    
    def setNome(self, valor): 
        self.__nome = valor
        
    #SEGUNDA FORMA DE USA RO GET E O SET.

    # CRIANDO O GET DO CARGO
    @property # Esse elemento irá criar um get mais amigável
    def cargo(self):
        return self.__cargo

    @cargo.setter # Essa forma irá criar um set para cargo mais amigável
    def cargo(self, info):
        self.__cargo = info  