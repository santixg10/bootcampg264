''' suma de los primeros n que diga el usuario '''
''' Con el ciclo for '''
num=int(input('Digite el limite de la suma: '))
suma=0
for i in range(1,(num+1),1):
    suma=suma+i
    i=i+1
print(f"la sumatoria es: {suma}")

''' Con el ciclo while '''

sum=0
cont=1
while cont<=num:
    sum+=cont
    cont=cont+1
print(f"La sumatoria con while es: {sum}")