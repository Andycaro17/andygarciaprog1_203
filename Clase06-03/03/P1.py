#Serie de números Fibonacci de largo arbitrario: Escribe un programa que imprima los primeros n números
#de la secuencia Fibonacci donde n es ingresado por el usuario



n1 = int(input("Digite un numero de inicio "))
n2 = int(input("Digite el numero de secuencia maxima "))

i = n1
j = i
cont = 0

print (n1) 
while True:
    i += j
    j += i
    cont += 2 
    if cont> n2:
       break
    print (i)
    print (j)
