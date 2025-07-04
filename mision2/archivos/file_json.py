import json #importamos el archivo json para poder usarlo
with open('mi_archivo.json', 'r') as file:
    data = json.load(file)#carga el archivo
print(data)
#para mirar las librerias instaladas es pip list
#para instalar librerias es pip install nombre de la libreria
#para desinstalar librerias es pip unstall nombre de la libreria
my_data = [{'nombre': 'juan', 'edad': 30, 'valor':789},
           {'nombre': 'Rose', 'edad': 23, 'valor':910}
           ]#se agrega otros datos
with open('otro_archivo.json', 'w') as file:#el file es como una variable entonces puede ser cualquier otra palabra
    json.dump(my_data, file, indent=4)#ese indent es para el espacio de izquierda a derech acomo la identacion
    #el dump es para sobreescribir un archivo