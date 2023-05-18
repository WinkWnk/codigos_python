while True:
    a = int(input("Informe um valor qualquer: "))
    b = int(input("Informe um outro valor qualquer diferente: "))

    if a != b:
        break
def somaImpar(inicial, final):
    soma = 0
    for cont in range(inicial, final+1):
        if cont % 2 ==1:
            soma += cont
    return soma

def mediaMultiplo3(inicial, final):
    total = 0
    contDivisores = 0
    for cont in range(inicial, final+1):
        if cont % 3 == 0:
            total += cont # Isto é para somar todos os divisores
            contDivisores += 1 # Isto é para contar todos os divisores
    return total / contDivisores

if a < b:
    print(f"A soma dos ímpares é: {somaImpar(a, b)}")
else:
    print(f"A média dos multiplos de 3 é: {mediaMultiplo3(b, a)}")

