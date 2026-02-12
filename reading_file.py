import os


#De esta manera se asigna a una variable el contenido de todo el archivo
def leer_todo(archivo):
    #Es muy buena práctica usar el bloque try catch
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró en la carpeta {os.getcwd()}.")

def leer_linea_por_linea(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            print(linea.strip())

def leer_lineas_lista(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        print(lineas[0])




archivo = 'prueba.txt'
#leer_todo(archivo)
#leer_linea_por_linea(archivo)
leer_lineas_lista(archivo)