#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False

def vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

print(vocal("hola"))
