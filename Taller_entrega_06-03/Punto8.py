#Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N

n1 = int(input("digite un numero "))

for i in range (1,n1+1):
   if n1%i==5:
      print(f"{i} es multiplo de 5")
 

      #if n1%i==0:
      #print(f"Los divisores de {n1} son {i}")