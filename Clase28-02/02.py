
# n1 = int(input("digite un numero "))

# for i in range (1,n1+1):
   #if n1%i==0:
      #print(f"{i} es divisor")
   #else:
      #print(i)



n1 = int(input("Digite un numero "))
cont = 0
for i in range (1,n1+1):
    if n1%i==0:
        cont+=1
        #print (f" {i} es primo")

if cont==2:
   print(f"El numero ingresasdo {n1} es primo")
   
else:
     print(f"El numero ingresasdo {n1} no es primo")










