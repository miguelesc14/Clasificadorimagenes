import time


def identificar(archivos):
    #print(archivos)
    def leer():
        with open("estado.txt", "w") as archivo:
            archivo.write(str("20"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("20%: Leyendo archivos"))


    def clasificar():
        with open("estado.txt", "w") as archivo:
            archivo.write(str("30"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("30%: Analizando archivos"))
        time.sleep(1)
        with open("estado.txt", "w") as archivo:
            archivo.write(str("45"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("45%: Analizando archivos"))

    def crear_carpetas():
        #print("75")
        with open("estado.txt", "w") as archivo:
            archivo.write(str("75"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("75%: Creando carpetas"))

    def asignar_carpetas():
        with open("estado.txt", "w") as archivo:
            archivo.write(str("90"))
        with open("mensaje.txt", "w") as archivo:
            archivo.write(str("90%: Asignando archivos"))

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