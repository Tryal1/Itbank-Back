import datetime
import os

def StartLog(nombre_log, nombre_archivo, dni, salida, status):
	""" Abre el archivo de log indicado. Devuelve el archivo abierto."""

	path = os.path.dirname(os.path.abspath(__file__))
	file_path = path + "\\" + nombre_log

	archivo_log = open(file_path, "a")

	hora_actual = str(datetime.datetime.now())

	archivo_log.write(f"{hora_actual}: IniScio de registro de actividad\n")
	archivo_log.write(f"{hora_actual} nombre del archivo: {nombre_archivo}  dni: {dni} - salida: {salida} - status: {status} \n")
	archivo_log.write(f"{hora_actual}: Fin de registro de actividad\n")

	archivo_log.close()
