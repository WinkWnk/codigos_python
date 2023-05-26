class Personagem:
    def __init__(self, nome):
        self._nome = nome 
        self._vida = 5

    def atacar(self):
        print(f"O personagem {self._nome} está atacando")

class Jogador(Personagem):
    def __init__(self, nome, tipoRaca):
        super().__init__(nome)
        self.__tipoRaca = tipoRaca

    def usarHabilidade(self, poder):
        self.__tipoRaca = poder
        print(f"Usando Hibilidade {self.__tipoRaca}")

    