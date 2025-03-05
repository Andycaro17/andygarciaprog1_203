#¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000? 


#for i in range (1,1001):
    #j = 2 
    #suma = 0 

    #if i%j==0:
        #suma+=1

#if suma==2:
   #print(f"{i} Es un numero primo")
   
cont = 0
j = 2

for i in range (1,1001):
    if i%j==0:
        cont+=1

if cont==2:
   print(f"El numero ingresasdo {i} es primo")
   
