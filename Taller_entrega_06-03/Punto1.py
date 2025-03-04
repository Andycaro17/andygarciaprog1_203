#Determinar los divisores de un número introducido por teclado

n1 = int(input("Digite un numero "))


for i in range (1,n1+1):
   if n1%i==0:
      print(f"Los divisores de {n1} son {i}")
   