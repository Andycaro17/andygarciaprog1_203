#Determinar cuales y cuantos números perfectos hay entre 1 y 1000? 


for i in range(1,1001):
    j = 2
    suma = 0
    while j <= i:
        if i % j == 0:
            suma += i // j 
        j += 1 
    if suma == i:
        print (i)



