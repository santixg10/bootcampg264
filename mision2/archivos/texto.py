archivo = open("mi_archivo.text", "w")#se crea el archivo
archivo.write("Esta es la primera linea. \n")#escribe en el archivo
archivo.write("Esta es la segunda linea. \n")

for i in range(3):#se escribe tres veces esta linea
    archivo.write(f"Esta es la linea {i+2}. \n")
archivo.close()#se cierra el archivo para poder usarse

archivo = open("mi_archivo.text", "r")#se lee lo que tiene el archivo
contenido = archivo.read()
print(contenido)# se muestra lo que tiene

for linea in contenido.split('\n'):#
    print(linea)