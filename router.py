import sys
import os
import clasificador

def rut():

    def el_inicio(ruta):
        # Obtención de lista con archivos
        try:
            archivos = [archivo for archivo in os.listdir(ruta) if
                        os.path.isfile(os.path.join(ruta, archivo))]
            clasificador.identificar(archivos)
        except FileNotFoundError:
            print("El directorio no existe.")

    i = 0
    ruta = ""

    while (i==0):
        try:
            if(os.path.exists("rutas.txt")):
                with open("rutas.txt", "r") as archivo:
                    ruta = archivo.read()

                if (ruta != ""):
                    i += 1
                    print("ruta= ", ruta)

                    el_inicio(ruta)

            else:
                #print("Aún no existe")
                #print(".")
                isa=0
        except FileNotFoundError:
            print("El directorio no existe.")
    sys.exit(0)