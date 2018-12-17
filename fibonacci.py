def ftfibonacci (nombre):
    i = 0
    j = 1
    b = 1
    while b < nombre :
        result = i + j
        i = j
        j = result
        b+=1
    print result

nombre = input("Nombre d'excution :")

ftfibonacci(nombre)
