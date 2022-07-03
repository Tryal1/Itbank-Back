# Itbank-Back

En este repositorio existen cuatro archivos principales. 
 * listado_cheques.py
 * log.py
 * crear_cheques.py

## Modulos necesarios

Se utilizan las  siguientes librerias para ejecutar el programa:

```python
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
# para crear registros de cheques
from crear_cheques import CrearCheques
```

## listado_cheques.py

```python
# Lee un archivo csv, y en caso de que exista, devuelve un arrelgo
LeerArchivo()

# Filtra un arreglo, en base a diferentes condiciones en caso de que existan
FiltrarArchivo()

# En caso de que existan registros duplicados, o que no haya ningun "match" se levanta error
LevantarErrores()

# Devuelve la lista de cheques que cumpla con los requisitos, ya sea por consola o exportando a un archivo csv
DevolverCheques()

# Crea o modifica un archivo csv, en donde le pasas valores por consola y los guarda
CrearCheques()

# Toma argumentos por consola, y ejecuta las funciones LeerArchivo(), FiltrarArchivo(), LevantarErrores() y DevolverCheques()
Main()

```

## log.py
```python
# registra en un archivo txt todas las veces que se ejecuta el programa, y el status de ejecución
StartLog()
```

## Contributing
Proyecto cerrado. Parte de Programa Fullstack Development ITBA


## License
[MIT](https://choosealicense.com/licenses/mit/)
