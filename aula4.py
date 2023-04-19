texto = "Técnico em desenvolvimento de sistemas"
print("*******Título*******")
print("*" *10)
print(texto)

idade = int(input("Qual é sua idade? "))
print("# "*idade)

#Manipulando textos(string)
print(f"O total de letras é {len(texto)}")  #len() vem de length, que significa total.

print(texto.upper())#upper() coloca todo o texto em caixa alta e lower() tudo em minúsculo.
print(texto.capitalize())#coloca a 1ª letra em maiúsculo

print(texto.replace("de sistemas","web")) #replace() faz uma troca de palavras.

#TRABALHANDO COM FATIAMENTO.
print("Fatiando a variável texto")
print(texto[:3])#Vai exibir todo o texto até a posição 2, no caso a posição 3 não conta.
print(texto[3:])#Vai exibir todo o texto a partir da posição 3.
print(texto[3:10])#Vai exibir todo o texto que está na posição 3 até 10. 