"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    # Abrimos el archivo
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para agrupar las letras por el valor de la columna 2
    grouped_data = {}

    for line in lines:
        # Dividimos cada línea por tabulaciones
        columns = line.strip().split("\t")
        letter = columns[0]  # Columna 0: Letra
        value = int(columns[1])  # Columna 1: Número

        # Añadimos al diccionario
        if value not in grouped_data:
            grouped_data[value] = []
        grouped_data[value].append(letter)

    # Ordenamos las claves (valores de columna 2) y construimos la lista final
    result = sorted(grouped_data.items())

    return result


# Llamar la función para ver la salida
print(pregunta_07())

