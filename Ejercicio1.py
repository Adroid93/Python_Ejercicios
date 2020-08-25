#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos

def max(n1,n2):
    mayor= n1
    if(n2>n1):
        mayor=n2
    else:
        mayor=n1
    return print("El mayor es: ",mayor)

print("Debe ingresar dos numeros enteros para determinar cual de ellos es mayor\n")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

max(numero1,numero2)