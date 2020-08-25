#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(n1,n2,n3):

    if(n2>n1 and n2>n3):
        mayor=n2
    elif(n3>n1 and n3>n2):
        mayor=n3
    else:
        mayor=n1

    return print("El mayor de los tres es: ",mayor)

print("Debe ingresar tres numeros enteros para determinar cual de ellos es mayor\n")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))

max_de_tres(numero1,numero2,numero3)