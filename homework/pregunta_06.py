"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    # Diccionario para almacenar el valor mínimo y máximo de cada clave
    claves = {}

    try:
        # Abrir el archivo y procesar línea por línea
        with open("files/input/data.csv", "r") as archivo:
            for linea in archivo:
                # Limpiar espacios y saltos de línea
                linea = linea.strip()
                # Dividir la línea por tabuladores
                columnas = linea.split("\t")
                
                if len(columnas) >= 5:
                    # Obtener la columna 5 que contiene el diccionario codificado
                    diccionario_str = columnas[4]
                    # Dividir el diccionario en pares clave:valor
                    claves_valores = diccionario_str.split(",")
                    
                    for clave_valor in claves_valores:
                        clave, valor = clave_valor.split(":")
                        valor = int(valor)  # Convertir el valor a entero

                        # Actualizar el diccionario con el valor mínimo y máximo
                        if clave not in claves:
                            claves[clave] = {"min": valor, "max": valor}
                        else:
                            if valor < claves[clave]["min"]:
                                claves[clave]["min"] = valor
                            if valor > claves[clave]["max"]:
                                claves[clave]["max"] = valor

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data.csv'. Verifica la ruta.")
        return []

    # Crear la lista de tuplas con las claves y sus valores mínimo y máximo
    resultado = [(clave, claves[clave]["min"], claves[clave]["max"]) for clave in sorted(claves.keys())]

    return resultado

# Llamar la función y mostrar el resultado
print(pregunta_06())
