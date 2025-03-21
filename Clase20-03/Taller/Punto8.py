#Moda


import random
cantidad=random.randint(5,15)
vector=[]


for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)
print(f"Elementos del vector {vector}")


        
mediana = 0

for i in vector:
    mediana = len(vector) // 2
        


print(vector [mediana])

