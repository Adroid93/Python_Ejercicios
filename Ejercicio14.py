'''
Dados dos números enteros determine los dígitos del primer número que están en el segundo
'''

numero1=int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
aux=numero1
digito=0
while(aux>0):

    digito=aux%10
    numero2%=10
    if(digito==numero2):
        print("hay coincidencia")
    else:
        print("no hay coincidencia")
    aux//=10
    numero2= numero2 %10