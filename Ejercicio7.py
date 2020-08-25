'''
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que
devolver True.
'''
def palindromo(cadena):
    posicion_derecha=len(cadena)-1
    posicion_izquierda=0
    while(posicion_izquierda>=posicion_derecha):
        if not(cadena[posicion_izquierda==cadena[posicion_derecha]]):
            return False
    posicion_izquierda+=1
    posicion_derecha-=1
    return True
print(palindromo("ana"))
