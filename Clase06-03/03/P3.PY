#->Descomposición en factores primos: Escribe un programa que descomponga un número n en sus factores primos, utilizando un ciclo while


#cont = 0
#n1 = int(input("Digite un numero "))

#while n1!= 0:
    #cont+=1
    #if cont==2: 
        #print(f"El numero ingresasdo {n1} es primo")
    #n2 = int(input("Digite un numero "))
#else:
     #print(f"El numero ingresasdo {n2} no es primo")

#///////////////////////////////////////////////////////////////////////////

cont = 0
n1 = int(input("Digite un numero "))

while n1!= 0:
    cont+=1
    if cont==2: 
        print(f"El numero ingresasdo {n1} no es primo")
    else:
     print(f"El numero ingresasdo {n1} es primo")
    n1 = int(input("Digite un numero "))

print ("El numero ingresado no es valido")