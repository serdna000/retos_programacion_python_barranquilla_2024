def es_triangulo(a, b, c):
    lista = [a, b, c]
    num_mayor = max(lista)
    suma_resto = sum(lista) - num_mayor

    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif num_mayor > suma_resto:
        return False
    else:
        return True
    
def es_equilatero(a, b, c):
    if a + b + c == 3*a:
        return True
    else:
        return False
    
def es_isoceles(a, b, c):
    if (a == b or a == c or b == c) and not(a + b + c == 3*a):
        return True
    else:
        return False

def es_escaleno(a, b, c):
    if not(a == b or a == c or b == c):
        return True
    else:
        return False
    
def es_rectangulo(a, b, c):
    lista = [a, b, c]
    hipotenusa = max(lista)
    lista.remove(hipotenusa)

    suma_lista_cuadrada = sum([num**2 for num in lista])

    if suma_lista_cuadrada == hipotenusa**2:
        return True
    else:
        return False