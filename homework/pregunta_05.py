"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    # Inicializar un diccionario para almacenar los valores de la columna 2 por letra
    datos = {}

    try:
        # Abrir el archivo y procesar línea por línea
        with open("files/input/data.csv", "r") as archivo:
            for linea in archivo:
                # Limpiar espacios y saltos de línea
                linea = linea.strip()
                # Dividir la línea por tabuladores
                columnas = linea.split("\t")
                
                if len(columnas) >= 2:
                    letra = columnas[0]  # Tomar la primera columna (letra)
                    valor = int(columnas[1])  # Tomar la segunda columna (valor) y convertir a entero

                    if letra not in datos:
                        datos[letra] = []  # Crear una lista vacía para la letra si no existe
                    datos[letra].append(valor)  # Agregar el valor de la columna 2

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data.csv'. Verifica la ruta.")
        return []

    # Crear la lista de tuplas con los resultados
    resultado = []
    for letra in sorted(datos.keys()):  # Ordenar por la letra
        max_valor = max(datos[letra])  # Obtener el valor máximo
        min_valor = min(datos[letra])  # Obtener el valor mínimo
        resultado.append((letra, max_valor, min_valor))

    return resultado

# Llamar la función y mostrar el resultado
print(pregunta_05())

