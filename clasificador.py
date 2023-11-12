import time
import os
import shutil
import datetime
import random

def identificar(archivos, ruta):
    print(archivos)

    # De prueba
    clases = ['animeplush','coche','persona','musica','gatos','aviones']
    clases_encontradas = []
    rutas_carpeta = []
    ruta_carpeta = ""

    def leer():
        with open("estado.txt", "w") as archivo:
            archivo.write(str("20"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("20%: Leyendo archivos"))
        print(archivos)


    def clasificar():
        with open("estado.txt", "w") as archivo:
            archivo.write(str("30"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("30%: Analizando archivos"))
        # Clasificar


        clase_actual = 'musica'

        nonlocal clases_encontradas
        clases_encontradas = ['musica']

        time.sleep(1)

        with open("estado.txt", "w") as archivo:
            archivo.write(str("45"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("45%: Analizando archivos"))

        for i in range(0, len(archivos)):
            # Renombrar
            ruta_imagen = ruta + '/' + archivos[i]

            extension = ruta_imagen.split('.')

            try:

                # Obtener la fecha de creación de la imagen
                fecha_creacion = os.path.getctime(ruta_imagen)
                fecha_formateada = datetime.datetime.fromtimestamp(fecha_creacion).strftime('%Y%m%d%H%M%S')

                # Renombrar archivo
                rad = str(
                    random.randint(1, 10))
                nuevo_nombre = ruta +'/'+ clase_actual + '_' + fecha_formateada + '_' + rad + '.' + \
                               extension[1]
                nn_abrev = clase_actual + '_' + fecha_formateada + '_' + rad + '.' + \
                               extension[1]
                archivos[i] = nn_abrev
                os.rename(ruta_imagen, nuevo_nombre)
                print("imagen_renombrada con el nombre " + nuevo_nombre)
            except FileNotFoundError:
                print("La imagen no existe.")


    def crear_carpetas():
        #print("75")
        with open("estado.txt", "w") as archivo:
            archivo.write(str("75"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("75%: Creando carpetas"))

        nonlocal ruta_carpeta
        nonlocal rutas_carpeta
        # Ruta y nombre de la carpeta a crear
        ruta_carpeta = ruta

        # Rutas por cada clase

        #print(clases_encontradas)

        rutas_carpeta = [ruta_carpeta+'/' + clases[i] for i in range(0, len(clases)) if clases[i] in clases_encontradas]

        #print(rutas_carpeta)

        # Verifica si ambas listas tienen mismo tamaño
        if (len(clases_encontradas) == len(rutas_carpeta)):
            for i in range(0, len(clases_encontradas)):
                # Creación de carpetas
                try:
                    os.mkdir(rutas_carpeta[i])
                    print("¡Carpeta " + clases_encontradas[i] + " creada con éxito!")
                except FileExistsError:
                    print("La carpeta " + clases_encontradas[i] + " ya existe.")
        else:
            print("Hay un error")


    def asignar_carpetas():
        with open("estado.txt", "w") as archivo:
            archivo.write(str("90"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("90%: Asignando archivos"))

        # mandar a carpetas

        # Lee por cada clase
        for j in range(0, len(clases_encontradas)):
            # Lee archivos
            for i in range(0, len(archivos)):
                # Si la clase esta contenida dentro del archivo actual
                if (clases_encontradas[j] in archivos[i]):
                    # Ruta y nombre del archivo a mover
                    ruta_archivo = ruta_carpeta+'/' + archivos[i]
                    # Ruta de destino (carpeta donde se moverá el archivo)
                    ruta_destino = rutas_carpeta[j]+'/' + archivos[i]
                    print(ruta_archivo)
                    print(ruta_destino)
                    # Mueve los archivos
                    try:
                        shutil.move(ruta_archivo, ruta_destino)
                        print("¡Archivo movido con éxito!")
                    except FileNotFoundError:
                        print("El archivo no existe.")
                else:
                    print("no se encontró: ",clases_encontradas[i]," != ",archivos[i])

    leer()
    time.sleep(1)
    clasificar()
    time.sleep(1)
    crear_carpetas()
    time.sleep(1)
    asignar_carpetas()
    time.sleep(1)

    with open("ban.txt", "w") as archivo:
        archivo.write(str("1"))