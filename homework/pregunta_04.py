"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    registros_por_mes = {str(i).zfill(2): 0 for i in range(1, 13)}  # Inicializar el contador para cada mes

    try:
        # Abrir el archivo y procesar línea por línea
        with open("files/input/data.csv", "r") as archivo:
            for linea in archivo:
                # Limpiar espacios y saltos de línea
                linea = linea.strip()
                # Dividir la línea por tabuladores
                columnas = linea.split("\t")
                
                if len(columnas) >= 3:
                    fecha = columnas[2]  # Tomar la tercera columna (fecha)
                    try:
                        # Extraer el mes de la fecha (formato YYYY-MM-DD)
                        mes = fecha.split("-")[1]
                        if mes in registros_por_mes:
                            registros_por_mes[mes] += 1
                    except IndexError:
                        continue  # Si la fecha no tiene el formato esperado, ignoramos la línea

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data.csv'. Verifica la ruta.")
        return []

    # Crear la lista de tuplas con los resultados, ordenados por mes
    resultado = sorted(registros_por_mes.items())

    return resultado

# Llamar la función y mostrar el resultado
print(pregunta_04())

