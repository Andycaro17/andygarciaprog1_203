#1. Ver posiciones pares e impares por separado
import random

cantidad = random.randint(1,15)
vector = []
pares = []
impares = []


for i in  range(len(vector)):
    if vector[i]%2==0:
        pares.append (vector[i])
    else:
        impares.append (vector[i])

print (vector)
print(f"numeros pares {pares}")
print(f"numeros impares {impares}")
