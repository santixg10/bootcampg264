import numpy as np #numpy  son las funciones aritmeticas somo sum, mean, std, median, etc
import matplotlib.pyplot as plt #para graficar

edades = [38, 25, 42, 18, 32, 16, 22, 43, 39, 27]
suma = np.sum(edades)
print("suma:", suma)
datos = np.count_nonzero(edades) #cuenta todos los numeros de la lista y si hay un cero no  lo cuenta
print("cantidad de datos: ",datos)
prom = np.mean(edades)
print("Promedio: ",prom)
me = np.median(edades)
print("Mediana: ",me)
minimo = np.min(edades)
print("Minimo: ",minimo)
maximo = np.max(edades)
print("Maximo: ",maximo)
desviacion = np.std(edades)
print("Desvacion Estandar: ",desviacion)
#linspace numero de puntos que queremos, 1= donde inica, 10= donde termina, 10=numero de puntos
#la x y la y tienen que tener la misma cantidad de puntos o de datos para que funcione
x = np.linspace(1, 10, 10) # 10 puntos entre 1 y 10
y = np.array(edades)

plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.title("Grafico con matplotlib")
plt.grid()#es la cuadricula de fondo
plt.show()