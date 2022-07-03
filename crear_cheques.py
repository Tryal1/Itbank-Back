import csv
import pathlib
from log import StartLog

def CrearCheques(NroCheque: str,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen ,NumeroCuentaDestino: str, valor ,fecha_origen: str, fecha_pago: str,dni: str, tipo_cheque: str, estado_cheque,nombre_archivo):
    fieldnames = ["NroCheque", "CodigoBanco", "CodigoScurusal", "NumeroCuentaOrigen",
                  "NumeroCuentaDestino", "Valor", "FechaOrigen", "FechaPago", "DNI", "Tipo", "Estado"]

    if not pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'w', newline='') as create_file:
            writer = csv.DictWriter(create_file, fieldnames=fieldnames,delimiter=';')
            writer.writeheader()

    with open(nombre_archivo, 'a', newline='') as escribir_csv:
        writer = csv.DictWriter(escribir_csv, fieldnames=fieldnames,delimiter=';')
        writer.writerow({"NroCheque": NroCheque,
                         "CodigoBanco":CodigoBanco ,
                         "CodigoScurusal": CodigoScurusal,
                         "NumeroCuentaOrigen": NumeroCuentaOrigen,
                         "NumeroCuentaDestino": NumeroCuentaDestino,
                         "Valor": valor,
                         "FechaOrigen": fecha_origen,
                         "FechaPago": fecha_pago,
                         "DNI": dni,
                         "Tipo": tipo_cheque,
                         "Estado": estado_cheque})
    StartLog(nombre_log="log.txt", nombre_archivo=nombre_archivo, dni=dni, salida='CREAR',
             cantidad_argumentos=12, status="SUCCESS")

    
