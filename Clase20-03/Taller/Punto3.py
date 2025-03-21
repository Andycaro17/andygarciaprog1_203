#Sumar valores pares

import random
cantidad=random.randint(5,15)
vector=[]
pares=[]

for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)
print(vector)


for i in range(len(vector)):
    if vector[i]%2==0:
        pares.append(vector[i])
        
print(f"Elementos pares {pares}")

spar= 0

for x in vector:
    if x%2==0:
        spar+=x
    

print(f"Suma de pares = {spar}")