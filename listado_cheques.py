# para leer el archivo csv
import csv
# para chequear si el archivo existe
import os
# para acceder a la fecha y hora actual
import datetime
# para copiar una lista
import copy
# para insertar argumentos desde consola
import sys
# para registrar las veces que se ejecuta el programa en un txt
from log import StartLog


PATH = os.path.dirname(os.path.abspath(__file__))
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

def LeerArchivo(nombre_archivo: str):
    """ Funcion que lee un archivo csv en caso que exista y lo devuelve en forma de lista. """

    FILE_PATH = PATH + "\\" + nombre_archivo

    if os.path.exists(FILE_PATH):

        with open(FILE_PATH, 'r') as input_csvfile:

            rows = []
            reader = csv.DictReader(input_csvfile, delimiter=';')
            for row in reader:
                rows.append(row)

        return rows

    else:

        print("Error: El archivo no existe. Por favor revisa si exisite el archivo, o bien, está bien escrito el nombre")
        


def FiltrarArchivo(rows: list, dni: str, tipo_cheque: str, estado_cheque = None, rango_fecha_inicio: str = None, rango_fecha_fin: str = None):
    """ Funcion que toma filtros opcionales y devuelve un objeto con los cheques que cumplen con los criterios. """

    filtered_rows = filter(lambda x: x["DNI"] == dni and x["Tipo"] == tipo_cheque, rows)
    filtered_rows = filter(lambda x: x["Estado"] == estado_cheque, filtered_rows) if estado_cheque else filtered_rows
    filtered_rows = filter(lambda x: x["FechaPago"] >= rango_fecha_inicio and x["FechaPago"] <= rango_fecha_fin, filtered_rows) if rango_fecha_inicio and rango_fecha_fin else filtered_rows

    return filtered_rows 



def LevantarErrores(filtered_rows):
    """ Funcion que levanta errores en caso de que haya registros duplicados o que no se encuentren resultados. """

    number_matches = copy.deepcopy(filtered_rows)
    number_matches = len(list(number_matches))

    if number_matches > 1:

        print("Error: se encontró más de un cheque con los criterios especificados")

        return 
        
    elif number_matches == 0:

        print("Error: no se encontró ningún cheque con los criterios especificados")

        return 

    elif number_matches == 1:

        return True


def DevolverCheques(filtered_rows, salida: str, dni: str):

    if salida == "PANTALLA":

        for filtered_row in filtered_rows:

            print(filtered_row)

    elif salida == "CSV":
        
        with open(PATH+"\\"+f"{dni}_{TIMESTAMP}.csv", 'w', newline='') as output_csvfile:
            
            fieldnames = ['FechaOrigen', 'FechaPago', 'Valor', 'NumeroCuentaOrigen']

            def DesiredValues(x): 

                return {k: v for k, v in x.items() if k in fieldnames}
            
            filtered_rows = list(map(DesiredValues, filtered_rows))

            writer = csv.DictWriter(output_csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
            
            print(f"Se ha creado el archivo {dni}{TIMESTAMP}.csv")


def Main(nombre_archivo: str, dni: str, salida: str, tipo_cheque: str, estado_cheque = None, rango_fecha_inicio: str = None, rango_fecha_fin: str = None):

    # Leer archivo csv
    rows = LeerArchivo(nombre_archivo)

    # Filtrar archivo csv
    filtered_rows = FiltrarArchivo(rows, dni = dni, tipo_cheque = tipo_cheque, estado_cheque = estado_cheque, rango_fecha_inicio = rango_fecha_inicio, rango_fecha_fin = rango_fecha_fin)

    # Levantar errores
    status = LevantarErrores(filtered_rows)

    # Devolver cheques
    DevolverCheques(filtered_rows, salida = salida, dni = dni) if status else None

    # Registro de fin y status del programa
    StartLog(nombre_log = "log.txt", nombre_archivo = nombre_archivo, dni = dni, salida = salida, cantidad_argumentos = len(sys.argv), status = "SUCCESS" if status else "FAIL")

# para probar el código
# python listado_cheques.py test.csv 11580999 PANTALLA EMITIDO APROBADO 1620183365 1620183375 -> Utilizando filtros opcionales de estado y rango de fecha (caso exitoso)
# python listado_cheques.py test.csv 11580999 PANTALLA EMITIDO APROBADO -> Utilizando filtro opcional de estado  y salida = CSV (caso exitoso)
# python listado_cheques.py test.csv 11580999 PANTALLA EMITIDO -> Sin utilizar los filtros opcionales (caso exitoso)

if __name__ == "__main__":

    if len (sys.argv) == 8:

        Main(nombre_archivo = sys.argv[1], dni = sys.argv[2], salida = sys.argv[3], tipo_cheque = sys.argv[4], estado_cheque = sys.argv[5], rango_fecha_inicio = sys.argv[6], rango_fecha_fin = sys.argv[7])

    elif len (sys.argv) == 6:

        Main(nombre_archivo = sys.argv[1], dni = sys.argv[2], salida = sys.argv[3], tipo_cheque = sys.argv[4], estado_cheque = sys.argv[5])

    elif len (sys.argv) == 5:

         Main(nombre_archivo = sys.argv[1], dni = sys.argv[2], salida = sys.argv[3], tipo_cheque = sys.argv[4])
    
    else:

        print("Error: El número de argumentos es incorrecto")