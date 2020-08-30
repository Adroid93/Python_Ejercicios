'''
Dado un número entero determinar si es igual al derecho y al revés
(capicúa), por ejemplo 1331, 55, 18981.
'''
reves=0
digito=0
aux=0;

numero=int(input("Ingrese un numero: "))
aux=numero
while(aux>0):
    digito=aux%10
    aux//=10
    reves=reves*10+digito

if(numero==reves):
    print("es capicua")
else:
    print("no es capicua")