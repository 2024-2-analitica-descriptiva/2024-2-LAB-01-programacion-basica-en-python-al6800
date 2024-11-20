"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    # Abrimos el archivo
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para agrupar las letras únicas y ordenadas por el valor de la columna 2
    grouped_data = {}

    for line in lines:
        # Dividimos cada línea por tabulaciones
        columns = line.strip().split("\t")
        letter = columns[0]  # Columna 0: Letra
        value = int(columns[1])  # Columna 1: Número

        # Añadimos al diccionario
        if value not in grouped_data:
            grouped_data[value] = set()
        grouped_data[value].add(letter)

    # Construimos la lista de tuplas, ordenando las letras para cada valor de columna 2
    result = [(key, sorted(list(value))) for key, value in sorted(grouped_data.items())]

    return result


# Llamar a la función para ver la salida
print(pregunta_08())

