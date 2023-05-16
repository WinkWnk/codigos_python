lista = ["João", 30, "Cohab"]
pessoa = {
    "nome":"Maria",
    "idade":24,
    "bairro":"Renascença"
}

print(lista[0])
print(pessoa, "\n")

#Exibindo as chaves utilizando o comando keys()
print(pessoa.keys())

#Exibindo os valores utilizando o comando values()
print(pessoa.values())

#Exibindo tanto a chave como valor utilizando o comando items()
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
