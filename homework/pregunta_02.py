"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    conteo = {}
    
    # Abrir el archivo y procesar línea por línea
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Suponemos que la primera columna está separada por comas
            columnas = linea.strip().split(",")  # Cambia si el separador es otro
            if columnas:  # Asegurarse de que la línea no esté vacía
                letra = columnas[0][0].upper()  # Tomamos la primera letra y la convertimos a mayúscula
                if letra.isalpha():  # Verificamos que sea una letra
                    conteo[letra] = conteo.get(letra, 0) + 1
    
    # Ordenamos el diccionario por las letras y convertimos a lista de tuplas
    resultado = sorted(conteo.items())

    return resultado

# Llamar la función y mostrar el resultado
print(pregunta_02())

