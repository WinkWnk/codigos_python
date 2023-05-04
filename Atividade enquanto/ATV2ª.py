maior = 0 

while True:
    num = int(input("Informe números inteiros: "))

    if num == 0:
        break

    if num > maior:
        maior = num
print(f"O maior número lido foi {maior}\n")


'''
maior = 0
while True:
    num = int(input("informe um valor: "))
    if num >= maior:
        maior = num
    if num == 0:
        break
print(f"O maior valor digitado foi {maior}")

'''