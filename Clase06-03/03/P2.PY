#Adivina el número: Escribe un programa que permita al usuario adivinar un número entre 1 y 100, 
#generando un número aleatorio. El ciclo debe continuar pidiendo al usuario adivinaciones hasta que adivine correctamente

import random

n = 1
cont = 0
num = random.randint(1,100)
while num!= n:
    n = int(input ("Digite un numero ")) 
   

print (f"Acertaste el numero ")