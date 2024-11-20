"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    suma_por_letra = {}

    try:
        # Abrir el archivo y procesar línea por línea
        with open("files/input/data.csv", "r") as archivo:
            for linea in archivo:
                # Limpiar espacios y saltos de línea
                linea = linea.strip()
                # Dividir la línea por tabuladores (como veo en tus datos, está separada por tabuladores)
                columnas = linea.split("\t")
                
                if len(columnas) >= 2:
                    letra = columnas[0]  # Tomar la primera columna (letra)
                    try:
                        valor_columna_2 = int(columnas[1])  # Convertir el valor de la segunda columna a entero
                    except ValueError:
                        continue  # Si no es un número válido, ignoramos la línea
                    
                    if letra.isalpha():  # Asegurarnos que es una letra
                        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna_2

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data.csv'. Verifica la ruta.")
        return []

    # Ordenar por la letra alfabéticamente
    resultado = sorted(suma_por_letra.items())

    return resultado

# Llamar la función y mostrar el resultado
print(pregunta_03())


