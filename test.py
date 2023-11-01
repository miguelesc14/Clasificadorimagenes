import tkinter as tk

class Modelo:
    def __init__(self):
        self.datos = []

    def agregar_dato(self, dato):
        self.datos.append(dato)

    def obtener_datos(self):
        return self.datos

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.label = tk.Label(self.ventana, text="Datos:")
        self.label.pack()

        self.entry = tk.Entry(self.ventana)
        self.entry.pack()

        self.boton = tk.Button(self.ventana, text="Agregar", command=self.agregar_dato)
        self.boton.pack()

    def agregar_dato(self):
        dato = self.entry.get()
        self.controlador.agregar_dato(dato)
        self.actualizar_vista()

    def actualizar_vista(self):
        datos = self.controlador.obtener_datos()
        self.label.config(text="Datos: " + ", ".join(datos))

    def iniciar(self):
        self.ventana.mainloop()

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar_dato(self, dato):
        self.modelo.agregar_dato(dato)
        self.vista.actualizar_vista()

modelo = Modelo()
vista = Vista(Controlador(modelo, vista))
vista.iniciar()