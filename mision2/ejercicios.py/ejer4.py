num1=int(input('Digite un numero: '))
num2=int(input('Digite un numero: '))

resultado = num1*num2
print("resultado de la multiplicacion: ",resultado)
cont = 0
for i in range(1,(num2+1),1):
    cont=cont+num1
    i=i+1
print("El ejercicio es: ",cont)