import os
import sys
import interfaz
import router

import threading
import time

# Función que se ejecutará en el subproceso
def programa_secundario():
    interfaz.gui()
    while True:
        print("Ejecutando programa secundario...")
        time.sleep(1)

# Función principal que ejecuta el programa con la GUI
def programa_principal():
    router.rut()
    while True:
        print("Ejecutando programa principal...")
        time.sleep(1)




# Crear y ejecutar los subprocesos
subproceso_secundario = threading.Thread(target=programa_secundario)
subproceso_secundario.start()

programa_principal()

