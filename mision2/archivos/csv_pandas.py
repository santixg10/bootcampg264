import pandas as pd#importamos la libreria y usamos un alias para identificar la libreria que es pd
df = pd.read_csv("cinema.csv")#df=data fream es una estructura tabular para mostrar datos como en excel, y quedan listos para manipularlos
print(df)# me muestra todas las columnas y filas
print(df['Age'])#me muestra solo la fila de Age
columnas_a_imprimir = ['Ticket_ID', 'Age', 'Ticket_Price']#una variable que va a imprimir esos apartados del archivo de excel
df_selec = df[columnas_a_imprimir]# me lo acomoda para una mejor visualizacion ya que esta con df
print(df_selec)