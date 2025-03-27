#Sacar el promedio de cada uno y decir si está por encima o por debajo del promedio de las listas juntas


import random


def llenar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]


def calcular_promedio(lista):
    return sum(lista) / len(lista)


def comparar_promedios():
    n = random.randint(5, 20)
    print(f"El tamaño de los arreglos es: {n}")
    

    arreglo1 = llenar_arreglo(n)
    arreglo2 = llenar_arreglo(n)
    
  
    promedio_arreglo1 = calcular_promedio(arreglo1)
    promedio_arreglo2 = calcular_promedio(arreglo2)
    
  
    promedio_total = calcular_promedio(arreglo1 + arreglo2)
    
  
    print("Arreglo 1:", arreglo1)
    print("Promedio Arreglo 1:", promedio_arreglo1)
    
    print("Arreglo 2:", arreglo2)
    print("Promedio Arreglo 2:", promedio_arreglo2)
    
    print("Promedio total de ambos arreglos:", promedio_total)
    

    if promedio_arreglo1 > promedio_total:
        print("El promedio del Arreglo 1 está por encima del promedio total.")
    else:
        print("El promedio del Arreglo 1 está por debajo del promedio total.")
    
    if promedio_arreglo2 > promedio_total:
        print("El promedio del Arreglo 2 está por encima del promedio total.")
    else:
        print("El promedio del Arreglo 2 está por debajo del promedio total.")

comparar_promedios()