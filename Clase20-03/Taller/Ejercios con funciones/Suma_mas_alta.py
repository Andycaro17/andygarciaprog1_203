
#Cuál de los dos tiene la suma más alta


import random


def llenar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]  


def comparar_sumas(n):
    arreglo1 = llenar_arreglo(n)
    arreglo2 = llenar_arreglo(n)
    
    suma1 = sum(arreglo1)
    suma2 = sum(arreglo2)
    
    print("Arreglo 1:", arreglo1)
    print("Arreglo 2:", arreglo2)
    
    if suma1 > suma2:
        print(f"El arreglo 1 tiene la suma más alta: {suma1}")
    elif suma2 > suma1:
        print(f"El arreglo 2 tiene la suma más alta: {suma2}")
    else:
        print("Ambos arreglos tienen la misma suma.")
        

n = 7
comparar_sumas(n)