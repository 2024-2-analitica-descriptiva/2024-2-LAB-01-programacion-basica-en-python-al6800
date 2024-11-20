"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    # Abrimos el archivo
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para almacenar las sumas
    result = {}

    for line in lines:
        # Dividimos la línea por tabulaciones
        columns = line.strip().split("\t")
        column_1 = columns[0]  # Columna 1: letra
        column_5 = columns[4]  # Columna 5: claves y valores separados por ":"

        # Extraemos los valores de la columna 5 y los sumamos
        sum_values = sum(int(item.split(":")[1]) for item in column_5.split(","))

        # Sumamos al total de la letra en el diccionario
        if column_1 in result:
            result[column_1] += sum_values
        else:
            result[column_1] = sum_values

    # Devolvemos el diccionario
    return result


# Llamar a la función para ver la salida
print(pregunta_12())

