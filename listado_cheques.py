import csv
import os
from log import StartLog
import datetime
import copy
import sys


def FiltrarCheque(nombre_archivo: str, dni: str, salida: str, tipo_cheque: str, estado_cheque = None, rango_fecha_inicio: str = None, rango_fecha_fin: str = None):
    """ Funcion que filtra cheques en base a un archivo csv y una lista de parametros. """

    path = os.path.dirname(os.path.abspath(__file__))
    file_path = path + "\\" + nombre_archivo

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    if os.path.exists(file_path):
        
        rows = []
        with open(file_path, 'r') as input_csvfile:

            reader = csv.DictReader(input_csvfile, delimiter=';')
            for row in reader:
                rows.append(row)
        

        filtered_rows = filter(lambda x: x["DNI"] == dni and x["Tipo"] == tipo_cheque, rows)
        filtered_rows = filter(lambda x: x["Estado"] == estado_cheque, filtered_rows) if estado_cheque else filtered_rows
        filtered_rows = filter(lambda x: x["FechaPago"] >= rango_fecha_inicio and x["FechaPago"] <= rango_fecha_fin, filtered_rows) if rango_fecha_inicio and rango_fecha_fin else filtered_rows

        number_matches = copy.deepcopy(filtered_rows)
        number_matches = len(list(number_matches))

        if number_matches > 1:

            print("Error: se encontró más de un cheque con los criterios especificados")
            StartLog("log.txt", nombre_archivo, dni, salida, "FAILED")
            return
        
        elif number_matches == 0:

            print("Error: no se encontró ningún cheque con los criterios especificados")
            StartLog("log.txt", nombre_archivo, dni, salida, "FAILED")
            return

        elif number_matches == 1:

            if salida == "PANTALLA":

                for filtered_row in filtered_rows:

                    print(filtered_row)

            elif salida == "CSV":
                
                with open(path+"\\"+f"{dni}_{timestamp}.csv", 'w', newline='') as output_csvfile:
                    
                    
                    fieldnames = ['FechaOrigen', 'FechaPago', 'Valor', 'NumeroCuentaOrigen']

                    def DesiredValues(x): 

                        return {k: v for k, v in x.items() if k in fieldnames}
                    
                    filtered_rows = list(map(DesiredValues, filtered_rows))

                    writer = csv.DictWriter(output_csvfile, fieldnames = fieldnames)
                    writer.writeheader()
                    writer.writerows(filtered_rows)
                    
                    print(f"Se ha creado el archivo {dni}{timestamp}.csv")
                    StartLog("log.txt", nombre_archivo, dni, salida, "SUCCESS")

    else:

        print("Error: El archivo no existe. Por favor revisa si exisite el archivo, o bien, está bien escrito el nombre")


#FiltrarCheque("test.csv", "11580999", "PANTALLA", "EMITIDO", "APROBADO", ["1620183365", "1620183375"])
if __name__ == "__main__":

    if len (sys.argv) == 7:

        FiltrarCheque(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

    elif len (sys.argv) == 6:

        FiltrarCheque(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

    elif len (sys.argv) == 5:

        FiltrarCheque(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])