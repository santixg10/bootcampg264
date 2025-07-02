num=int(input('Digite el limite de la suma de los cuadrados: '))
suma=0
for i in range(1,(num+1),1):
    suma=suma+i**2
    i=i+1
print("la sumatoria de los cuadrados es: ",suma)