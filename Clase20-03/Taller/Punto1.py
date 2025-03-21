#Ver posiciones pares e impares por separado

import random

cantidad=random.randint(5,15)
vector=[]
pares = []
impares = []

for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)

print(vector)

for i in range(len(vector)):
    if vector[i]%2==0:
        pares.append(vector[i])
    else:
        impares.append(vector[i])

print(f"numeros pares {pares}")
print(f"numeros impares {impares}")