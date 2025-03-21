#Mayor


import random
cantidad=random.randint(5,15)
vector=[]
pares=[]
impares=[]

for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)
print(f"Elementos del vector {vector}")


for i in range(len(vector)):
    if vector[i]%2==0:
        pares.append(vector[i])
    else:
        impares.append(vector[i])
        
print(f"Elementos pares {pares}")
print(f"Elementos impares {impares}")

spar = 0
dpar= 0
simp = 0
dimp = 0

for x in vector:
    if x%2==0:
        spar+=x
        dpar = spar // len(pares)
        

    else:
        simp += x
        dimp = simp // len(impares)


print(f"Suma de pares = {spar}")
print(f"Suma de impares = {simp}")

print(f"Promedio de elementos pares = {dpar}")
print(f"Suma de de elementos impares = {dimp}") 


