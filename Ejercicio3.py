#Definir una función que calcule la longitud de una lista o una cadena dada

def longitud(cadena):
    recorrido=0
    for i in cadena:
        recorrido+=1
    return print("Su longitud es: ",recorrido)

cadena= input("Ingrese una frase:")
longitud(cadena)