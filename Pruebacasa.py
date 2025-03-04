import random

n = 1
cont = 0
num = random.randint(1,20)
print (num)
while num!= n:
    n = int(input ("Digite un numero ")) 
    cont+=1

print (f"Numero de intentos {cont} ")