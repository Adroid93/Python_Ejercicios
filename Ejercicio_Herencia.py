from math import *
class Calculadora:

    def __init__(self,numero):
        self.n=numero
        self.datos= [0 for i in range(numero)]

        '''def ingresar(self):
            self.datos=[int(input("Ingresar datos "+str(i+1)+"="))for i in range(self.n)]
            '''

class Operaciones_Basicas(Calculadora):

    def __init__(self):
        Calculadora.__init__(self,2)

    def ingresar(self):
        self.datos = [int(input("Ingresar datos " + str(i + 1) + "=")) for i in range(self.n)]

    def suma(self):
        a,b,=self.datos
        resultado= a+b
        print("El resultado es: ",resultado)

    def resta(self):
        a,b,=self.datos
        resultado= a-b
        print("El resultado es: ",resultado)

class raiz(Calculadora):

    def __init__(self):
        Calculadora.__init__(self,1)

    def raiz_cuadrada(self):
        a,= self.datos
        print("El resultado es: ",sqrt(a))

ejemplo=Operaciones_Basicas()
print(ejemplo.ingresar())
print(ejemplo.suma())
