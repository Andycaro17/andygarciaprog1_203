#lista = []

#cantidad = int(input("Que cantidad de numeros "))

#for i in range (cantidad):
    #num = int(input("Digite numero "))
    #lista.append(num)

#print(lista)


#//////////////////////////////////////////////////////////////////////////
# Genera lista de numeros aleatorios
#import random

#cantidad = random.randint(1,15)
#vector = []

#for i in  range (cantidad):
    #num=random.randint (1, 100)
    #vector.append (num) # La funcion append es para ingresar elementos a la lista

#print (vector)
#print (len(vector)) #l a funcion len muestra el numero de elementos de la lista

#//////////////////////////////////////////////////////////////////////////

#Mostrar solo los elementos ubicados en indices pares
#import random

#cantidad = random.randint(1,15)
#vector = []

#for i in  range (len(vector)):
    #if i%2==0:
        #print (vector [i], end=" ")
   
#print()

#for i in range (0, len(vector), 2):
    #print (vector [i], end=" ")

#//////////////////////////////////////////////////////////////////////////

#Mostrar solo los elementos ubicados en indices impares

#import random

#cantidad = random.randint(1,15)
#vector = []

#for i in  range (len(vector)):
    #if i%2!=0:
        #print (vector [i], end=" ")
   
#print()

#for i in range (1, len(vector), 2):
    #print (vector [i], end=" ")


#//////////////////////////////////////////////////////////////////////////

# Mostrar numeros pares del contenido del vector

import random

cantidad = random.randint(5,15)
vector = []
pares = []
impares = []


for i in  range(len(vector)):
    if vector[i]%2==0:
        pares.append (vector[i])
    else:
        impares.append (vector[i])

print (vector)
print(pares)
print ()
print(impares)

