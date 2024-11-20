"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    # Abrimos el archivo
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para almacenar las sumas
    result = {}

    for line in lines:
        # Dividimos la línea por tabulaciones
        columns = line.strip().split("\t")
        column_2 = int(columns[1])  # Columna 2: número
        column_4 = columns[3]  # Columna 4: lista de letras separadas por comas

        # Para cada letra en la columna 4, sumamos el valor de la columna 2
        for letter in column_4.split(","):
            if letter in result:
                result[letter] += column_2
            else:
                result[letter] = column_2

    # Ordenamos el diccionario alfabéticamente por las claves
    sorted_result = dict(sorted(result.items()))

    return sorted_result


# Llamar a la función para ver la salida
print(pregunta_11())

