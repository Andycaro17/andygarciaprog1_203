#if True:
    #print("Esto ocurre una sola vez")

#cont = 0

#while  True: 
    #print("Este ciclo es infinito")
    #cont+=1
    #if cont == 5:
        #break


#num = 1
#cont = 0
#while num!= 0:
    #num = int(input("Digite un numero "))
    #cont+=1 

#print (f"Usted ingreso {cont} numeros") 


import random

n = 1
cont = 0
num = random.randint(1,20)
print (num)
while num!= n:
    n = int(input ("Digite un numero ")) 
    cont+=1

print (f"Numero de intentos {cont} ")