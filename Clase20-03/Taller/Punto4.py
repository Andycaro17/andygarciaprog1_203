#Sumar valores impares


import random
cantidad=random.randint(5,15)
vector=[]
impares=[]


for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)
print(vector)


for i in range(len(vector)):
    if vector[i]%2!=0:
        impares.append(vector[i])
    
    
print(f"Elementos impares {impares}")

simp = 0

for x in vector:
    if x%2!=0:
        simp += x
 
        
print(f"Suma de impares = {simp}")