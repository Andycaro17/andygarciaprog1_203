#promedio

import random

def generar_y_promediar(inferior, superior, cantidad):
   
    cantidad = random.randint(*cantidad)  
    lista_aleatoria = [random.randint(inferior, superior) for _ in range(cantidad)]
    promedio = sum(lista_aleatoria) / len(lista_aleatoria) 
    
    return lista_aleatoria, promedio


inferior = 1  
superior = 100  
cantidad = (5, 20)  


lista, promedio = generar_y_promediar(inferior, superior, cantidad)


print(f"Lista de números aleatorios: {lista}")
print(f"Promedio de los números: {promedio}")

