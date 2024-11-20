"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    # Abrimos el archivo
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Lista para almacenar el resultado
    result = []

    for line in lines:
        # Dividimos la línea por tabulaciones
        columns = line.strip().split("\t")
        column_1 = columns[0]  # Columna 1: letra
        column_4 = columns[3]  # Columna 4: lista separada por ","
        column_5 = columns[4]  # Columna 5: lista separada por ","

        # Contamos los elementos en las columnas 4 y 5
        count_column_4 = len(column_4.split(","))
        count_column_5 = len(column_5.split(","))

        # Añadimos la tupla a la lista de resultados
        result.append((column_1, count_column_4, count_column_5))

    return result


# Llamar a la función para ver la salida
print(pregunta_10())
