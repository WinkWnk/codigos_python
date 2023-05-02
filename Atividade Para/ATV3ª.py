valor = int(input("Informe um valor: "))

for contador in range (1, valor+1):
    if(valor % contador == 0):
        print(contador)