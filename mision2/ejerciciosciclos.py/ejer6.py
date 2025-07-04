salario=int(input("Digite la tarifa de pago: "))
dias=['lunes','martes','miercoles','jueves','viernes']
horas=0
for i in range(0,(len(dias)),1):
    horasextras= int(input(f'Digite cuantas horas extras trabajo el dia {dias[i]}: '))
    horas+=(salario*horasextras)
print("Valor total a pagar: ",horas)