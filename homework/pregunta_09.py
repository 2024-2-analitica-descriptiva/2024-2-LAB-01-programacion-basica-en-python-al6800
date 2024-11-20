"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    # Abrimos el archivo
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para contar ocurrencias de claves de la columna 5
    key_count = {}

    for line in lines:
        # Dividimos cada línea por tabulaciones
        columns = line.strip().split("\t")
        column_5 = columns[4]  # Columna 5: claves separadas por ","

        # Procesamos cada clave en la columna 5
        for pair in column_5.split(","):
            key = pair.split(":")[0]  # Extraemos la clave (antes de ":")
            key_count[key] = key_count.get(key, 0) + 1  # Incrementamos el contador

    return key_count


# Llamar a la función para ver la salida
print(pregunta_09())

