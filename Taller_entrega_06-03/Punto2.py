#Determinar si un numero es o no es primo 

n1 = int(input("Digite un numero "))
cont = 0
for i in range (1,n1+1):
    if n1%i==0:
        cont+=1

if cont==2:
   print(f"El numero ingresasdo {n1} es primo")
   
else:
     print(f"El numero ingresasdo {n1} no es primo")