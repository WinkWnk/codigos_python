
class Calculadora:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0

    def soma(self, valor1, valor2):
        self.__num1 = valor1
        self.__num2 = valor2
        print(f"{self.__num1 + self.__num2}")

    def subtrair(self, valor1, valor2):
        self.__num1 = valor1
        self.__num2 = valor2
        print(f"{self.__num1 - self.__num2}")


    def multiplicar(self, valor1, valor2):
        self.__num1 = valor1
        self.__num2 = valor2
        print(f"{self.__num1 * self.__num2}")

    def dividir(self,valor1, valor2):
        self.__num1 = valor1
        self.__num2 = valor2
        print(f"{self.__num1 / self.__num2}")



'''
class Calculadora:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0

    def somar(self, valor1, valor2):
        self.__num1 = valor1
        self.__num2 = valor2

        print(f"A soma é {self.__num1 + self.__num2}\n")
'''


