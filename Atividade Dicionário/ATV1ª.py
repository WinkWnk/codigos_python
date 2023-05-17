lista = list()
produtos = dict()

for contador in range (0,5):
    nome = input("Informe o nome do produto: ")
    produtos[nome] = int(input(f"Informe a quantidade de {nome}: "))

    lista.append(produtos.copy()) #copiar o conteúdo do diocionário para a lista
    produtos.clear() # limpar o conteúdo do diocionário

print(lista)