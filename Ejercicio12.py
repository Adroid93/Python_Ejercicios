'''
Leer un número entero y determinar si es perfecto
(es decir, es igual a la suma de sus divisores sin incluirlo, como el 6 = 1+2+3 y el 28 =1+2+4+7+14
'''
numero= int(input("Ingrese un numero: "))

divisor=1
sumadiv=0
for i in range(1,numero):
    if(numero%i==0):
        sumadiv+=i
if(numero==sumadiv):
    print("es perfecto")
else:
    print("no es perfecto")