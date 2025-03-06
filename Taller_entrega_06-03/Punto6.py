# Calcular el máximo de números positivos introducidos por teclado, 
# sabiendo que metemos números hasta que introduzcamos uno negativo. El negativo no cuenta

n1 = int(input("Ingrese un numero "))
cont = 0

while n1>= 0:
    n1 = int(input ("Ingrese un numero ")) 
    cont+=1

print (f"Numeros positivos ingresados {cont} ")