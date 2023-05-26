from funcionario2 import Funcionario


class Funcionario:
    def __init__(self, cargo, nome):
        self._cargo = cargo # Protegidos por estarem apenas com um underline
        self._nome = nome

    def informacoes(self):
        print(f"Olá {self._nome} seu cargo atual é {self._cargo}\n")

class Gerente(Funcionario):
    def __init__(self, cargo, nome, salario):
      super().__init__(cargo, nome) # super() significa que estamos usando a superclasse
      self._salario = salario

    def exibirCoisas(self):
        print(f"Seu nome é {self._nome}, e você ganha {self._salario}")