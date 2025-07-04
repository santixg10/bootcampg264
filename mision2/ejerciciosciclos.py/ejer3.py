inicio=int(input('Digite el limite inferior de la suma: '))
fin=int(input('Digite el limite superior  de la suma: '))

if fin>inicio:
    suma=0
    for i in range(inicio,(fin+1),1):
        suma=suma+i
        i=i+1
    print("la sumatoria es: ",suma)
else:
    print("Tiene que ser el numero superior mayor que el numero inferior")
