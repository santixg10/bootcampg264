def mostrarmenu():
    menu = int(input('1. Calcular el producto de todos los elementos de una lista de n posiciones.\n \n' 
    '2. Calcular la suma de todos los elementos de una lista de n posiciones.\n \n' 
    '3. Buscar en una lista de elementos numéricos, los elementos mayores a un valor X ' 
    'dado por el usuario y mostrar cuantos se encontraron. \n \n ' 
    '4. Calcular la suma de todos los elementos de una lista en sus posiciones impares.\n \n'
    '5. Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos \n \n' 
    'negativos y cuantos son cero.' 
    '6. Calcular los cuadrados de todos los elementos de una lista.\n \n'
    '7. Determinar si un número X dado por el usuario se encuentra repetido o no en una lista' 
    'de elementos numéricos.\n \n' 
    '8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado ' 
    'por el usuario y mostrar las posiciones donde están ubicados.\n \n'
    '0.salir \n \n'
    'Digite cual ejercicio quiere: '))
    return menu


menu = mostrarmenu()
while (menu !=0):
    if menu == 1:
        lista=[]
        multi=1
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        if (tamaño !=0):
            for i in range (1,(tamaño+1),1):
                numeros=int(input("Ingrese los números de la lista: "))
                lista.append(numeros)#para meter lo solicitado en una lista osea en un vector
            print(lista)
            for j in range (0,len(lista),1):
                print(multi)
                multi = multi * lista[j]
            print("Este es el resultado de la multiplicacion de los elementos de la lista",multi)
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break  
        

    if menu ==2:
            tamañ=int(input("Ingrese el tamaño de la lista: "))
            if (tamañ !=0):
                list=[]
                sum=1
                for i in range (1,(tamañ+1),1):
                    numero=int(input("Ingrese los números de la lista: "))
                    list.append(numero)
                print(list)
                for j in range (0,len(list),1):
                    sum = sum + list[j]
                print("Este es el resultado de la suma de los elementos de la lista",sum)
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break         

    if menu ==3:
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        if (tamaño !=0):
            lista=[]
            sum=1
            for i in range (1,(tamaño+1),1):
                numero=int(input("Ingrese los números de la lista: "))
                lista.append(numero)
            print(lista)
            x=int(input("Ingrese el valor que quieras saber cuales son los numeros mayores a ese: "))
            cont=0
            for n in lista:
                if n>x:
                    cont=cont+1
            print("Este es el número de veces que se encontaron que cumplan con la condición: ",cont)
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break 
            
    if menu == 4:
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        if (tamaño !=0):
            lista=[]
            sum=0
            for i in range (1,(tamaño+1),1):
                numero=int(input("Ingrese los números de la lista: "))
                lista.append(numero)
            print(lista)
            
            for n in range (0,len(lista),2):
                    sum+=lista[n]
            print("Esta es la suma de las posiciones impares: ",sum)
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break 
            
    if menu == 5:
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        if (tamaño !=0):
            lista=[]
            for i in range (1,(tamaño+1),1):
                numero=int(input("Ingrese los números de la lista: "))
                lista.append(numero)
            print(lista)
            pos=0
            neg=0
            cer=0
            for n in range (0,len(lista),1):
                if lista[n]>0:
                    pos+=1
                if lista[n]<0:
                    neg+=1
                if lista[n]==0:
                    cer+=1 
            print("Esta es la cantidad de los números positivos: ",pos)
            print("Esta es la cantidad de los números negativos: ",neg)
            print("Esta es la cantidad de los números ceros: ",cer)
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break 
            
    if menu ==6:
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        if (tamaño !=0):
            lista=[]
            for i in range (1,(tamaño+1),1):
                numero=int(input("Ingrese los números de la lista: "))
                lista.append(numero)
            print(lista)
            potencia=0
            po=0
            pote=[]
            for n in range (0,len(lista),1):
                print(potencia)
                print("esto es n",n)
                potencia=(lista[n]**2)
                pote.append(potencia)
                po=po+1
                
            print(f"La lista es: {lista}, y sus cuadrados son: {pote}")
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break 
    if menu == 7:
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        if (tamaño !=0):
            lista=[]
            for i in range (1,(tamaño+1),1):
                numero=int(input("Ingrese los números de la lista: "))
                lista.append(numero)
            print(lista)
            x=int(input("Ingrese el numero que se quiere verificcar si se repite: "))
            cont=0
            for n in range (0,len(lista),1):
                if x==lista[n]:
                    cont=cont+1  
            print(f"Estas son las veces que se repite el numero {x}: las veces son: {cont} ")
            opcion=int(input("Quieres volver al menu? 1=si   2=no \n \n"))
            if opcion == 1:
                menu = mostrarmenu()
            if opcion == 2:
                break 



