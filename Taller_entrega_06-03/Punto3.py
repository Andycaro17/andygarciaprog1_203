#Determinar si un número es o no es perfecto. Un numero es perfecto si la suma de sus divisores sin incluir el propio número es igual 
#a este

n1 = int(input("Digite un numero "))
i = 2
suma = 0



while i <= n1:
    if n1%i==0:
        suma += n1 // i
    i += 1
if suma == n1:
    print (f"{n1} es un numero perfecto")
else:
    print (f"{n1} no es un numero perfecto")