a = float(input("Informe a lado A: "))
b = float(input("Informe a lado B: "))
c = float(input("Informe a lado C: "))

if a < b+c and b < a+c and c < a+b:
    print("Temos um triângulo\n")
else:
    print("Você não encontrou um triângulo\n")