b = int(input("Informe sua idade: "))

def idade (age):
    if age >= 5 and age <= 7:
        return("INFANTIL A")
    
    elif age >= 8 and age <= 10:
        return("INFANTIL B")
    
    elif age >= 11 and age <= 13:
        return("JUVENIL A")
    
    elif age >= 14 and age <= 17:
        return("JUVENIL B")
    
    elif age >= 18:
        return("ADULTO")

print(idade(b))