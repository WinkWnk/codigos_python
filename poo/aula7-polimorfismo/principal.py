from produto import Produto, Livro, Eletronico

meuLivro = Livro("Hoje é quinta", 56, "Fulano Cury")

valor = int(input("Digita qualquer valor seu otário: "))

meuEletronio = Eletronico("Máquina de cabelo", valor, "nike")

meuLivro.descrever()
meuLivro.calcularPreco()
meuEletronio.calcularPreco()