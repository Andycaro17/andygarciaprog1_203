#Mediana

import random


def generar_lista(n):
    return [random.randint(1, 100) for _ in range(n)]


def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 != 0:
        return lista_ordenada[n // 2]
    else:
        mid1 = n // 2
        mid2 = mid1 - 1
        return (lista_ordenada[mid1] + lista_ordenada[mid2]) / 2


def procesar_lista():
    n = random.randint(5, 20)
    print(f"El tamaño de la lista es: {n}")
    lista = generar_lista(n)
    mediana = calcular_mediana(lista)
    print("Lista generada:", lista)
    print(f"La mediana de la lista es: {mediana}")


procesar_lista()