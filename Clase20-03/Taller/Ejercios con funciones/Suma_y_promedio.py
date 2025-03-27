#Suma pares y promedio de los impares

import random


def generar_lista(n):
    return [random.randint(1, 100) for _ in range(n)]


def sumar_pares(lista):
    return sum(x for x in lista if x % 2 == 0)


def promedio_impares(lista):
    impares = [x for x in lista if x % 2 != 0]
    if impares: 
        return sum(impares) / len(impares)
    else:
        return 0  


def procesar_lista():
    
    n = random.randint(5, 20)
    print(f"El tamaño de la lista es: {n}")
    lista = generar_lista(n)
    suma_pares = sumar_pares(lista)
    promedio_impares_total = promedio_impares(lista)
    
    print("Lista generada:", lista)
    print(f"Suma de los números pares: {suma_pares}")
    print(f"Promedio de los números impares: {promedio_impares_total}")

procesar_lista()