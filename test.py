def ftfibonacci (nombre):
    i = 0
    j = 1
    b = 1
    while b <= nombre :
        temp = i + j
        i = j
        j = temp
        b+=1
    print temp

nombre = input("Nombre d'excution :") -1
ftfibonacci(nombre)
