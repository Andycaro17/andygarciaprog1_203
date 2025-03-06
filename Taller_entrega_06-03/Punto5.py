#¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000? 


n = 1 

while n <= 1000:
    cont = 1
    j = 0
    while cont <= n:
        if n % cont == 0:
            j = j + 1
        cont = cont + 1
    if j == 2:
        print (n)

    n = n + 1


