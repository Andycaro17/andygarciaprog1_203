#Cuál de los dos tiene el número menor


import random


def llenar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]  


def comparar_menores(n):
    arreglo1 = llenar_arreglo(n)
    arreglo2 = llenar_arreglo(n)
    
    min1 = min(arreglo1) 
    min2 = min(arreglo2)  
    
    print("Arreglo 1:", arreglo1)
    print("Arreglo 2:", arreglo2)
    
    if min1 < min2:
        print(f"El arreglo 1 tiene el número menor: {min1}")
    elif min2 < min1:
        print(f"El arreglo 2 tiene el número menor: {min2}")
    else:
        print("Ambos arreglos tienen el mismo número menor.")
        

n = 10 
comparar_menores(n)