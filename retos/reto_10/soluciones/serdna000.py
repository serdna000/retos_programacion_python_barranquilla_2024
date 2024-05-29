from sympy import primerange
from math import sqrt

#ejercicio 01
def cifras(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    lista_cifras = []

    while n > 0:
        lista_cifras.append(n % 10)
        n //= 10
    
    return lista_cifras

#ejercicio 02
def es_armstrong(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    lista_cifra = cifras(n)
    resultado = [num**len(lista_cifra) for num in lista_cifra]

    return sum(resultado) == n

#ejercicio 03
def es_feliz(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    resultado = n
    while True:
        lista_cifras = cifras(resultado)
        resultado = sum([num**2 for num in lista_cifras])
        if resultado == 1 or resultado == n:
            break
    
    if resultado == 1:
        return True
    else:
        return False

#ejercicio 04
def es_primo_feliz(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    lista_primos = list(primerange(1, n + 1))

    if n in lista_primos and es_feliz(n):
        return True
    else:
        return False

print(cifras(1234))
print(es_armstrong(4210818))
print(es_feliz(4))
print(es_primo_feliz(97))