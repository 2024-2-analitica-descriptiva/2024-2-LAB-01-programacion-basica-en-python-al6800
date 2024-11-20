"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    suma = 0
    try:
        with open("files/input/data.csv", "r") as archivo:  # Ruta correcta a 'files/data.csv'
            for linea in archivo:
                columnas = linea.strip().split("\t")  # Asumimos que las columnas están separadas por tabulaciones
                suma += int(columnas[1])  # Convertimos a entero y sumamos la segunda columna
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data.csv' en la carpeta 'files'. Verifica la ruta.")
        return None
    return suma

# Llama la función
print(pregunta_01())

