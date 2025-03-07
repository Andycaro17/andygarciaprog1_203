#->Descomposición en factores primos: Escribe un programa que descomponga un número n en sus factores primos, utilizando un ciclo while


n1 = int(input("Digite un numero "))

if n1 > 1:
     cont = 0
     i = 2 

     while i < n1 and cont == 0:
        resto = n1%i

        if resto == 0:
             cont+= 1
        i += 1

     if cont == 0:
      print (f"El numero ingresado {n1} es primo")

     else:
      print (f"El numero ingresado {n1} no es primo")
