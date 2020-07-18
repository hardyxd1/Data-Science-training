cadena= 'Hola mundo'

#Abrimos el archivos para escritura
#la w nos idica que es para escritura
archivo=open('miArchivo.txt', 'w') 

#Escribimos en ela rchivo
archivo.write(cadena)

#Cerramos el archivo
archivo.close()
