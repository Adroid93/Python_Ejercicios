'''
Dado un número entero, determine si es o no primo
(un número primo solo es divisible entre si mismo y la unidad)
'''
numero= int(input("Ingrese un numero: "))

divisor=2
contador=1
while(divisor<=9):
    if(numero%divisor==0):
        contador+=1
    divisor+=1
if(contador>3):
    print("El numero ingresado no es primo")
else:
    print("El numero ingresado es primo")