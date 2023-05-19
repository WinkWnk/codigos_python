class Aluno:
    def __init__(self, nome, matricula, telefone):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
    def exibirDados(self):
        print(f"Boas vindas {self.nome} - ({self.matricula}), seu telefone é {self.telefone}")