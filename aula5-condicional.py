notaone = float (input("Informe a nota 1: "))
notatwo = float (input("Informe a nota 2: "))

average = (notaone + notatwo)/2

if average >= 7: #"se" simples 
    print("Você passou :)\n")

elif average == 6: 
    print("Você está de recuperação!")

else: 
    print("Você ficou reprovado")


'''
else: 
    print ("Você reprovou :(\n")
'''