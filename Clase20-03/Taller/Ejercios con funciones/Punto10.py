#Varianza


import random

def generar_lista(n):
    return [random.randint(1, 100) for _ in range(n)]

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def calcular_varianza(lista):
    promedio = calcular_promedio(lista)
    varianza = sum((x - promedio) ** 2 for x in lista) / len(lista)
    return varianza

def procesar_lista():
    n = random.randint(5, 20)
    print(f"El tamaño de la lista es: {n}")
    
    lista = generar_lista(n)
    
    varianza = calcular_varianza(lista)
   
    print("Lista generada:", lista)
    print(f"La varianza de la lista es: {varianza}")

procesar_lista()