
# Cuál de los dos tiene el número mayor

import random


def llenar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]  

def comparar_maximos(n):
    arreglo1 = llenar_arreglo(n)
    arreglo2 = llenar_arreglo(n)
    
    max1 = max(arreglo1)  
    max2 = max(arreglo2)  
    
    print("Arreglo 1:", arreglo1)
    print("Arreglo 2:", arreglo2)
    
    if max1 > max2:
        print(f"El arreglo 1 tiene el número mayor: {max1}")
    elif max2 > max1:
        print(f"El arreglo 2 tiene el número mayor: {max2}")
    else:
        print("Ambos arreglos tienen el mismo número mayor.")
        

n = 10  
comparar_maximos(n)