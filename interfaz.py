import sys
import time
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import ttk
from ttkthemes import ThemedStyle

ruta = ""
with open("rutas.txt", "w") as archivo:
    archivo.write(str(""))

with open("estado.txt", "w") as archivo:
    archivo.write(str(""))
with open("mensaje.txt", "w") as archivo:
    archivo.write(str(""))
ban_ruta = 0
def gui():
    # Para cuando se pulse en el input
    def click(*args):
        input_entry.delete(0, 'end')


    def choose_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Hacer algo con la carpeta seleccionada
            ruta = folder_path

            #print(ruta)
            #print("Carpeta seleccionada:", folder_path)
            input_entry.delete(0, 'end')
            input_entry.insert(0, ruta)

    def save():
        #final_label.config(text="Nuevo texto")
        ruta = input_entry.get()
        with open("ban.txt", "w") as archivo:
            archivo.write(str("0"))
        with open("rutas.txt", "w") as archivo:
            archivo.write(str(ruta))
        input_entry.config(state="disabled")
        choose_folder_button.config(state="disabled")
        start_button.config(state="disabled")

        # Inicio
        barra_progreso['value'] = 0
        window.update_idletasks()
        progres_label.grid(row=6, column=1, padx=10, pady=10)
        progres_label.config(text="0%: Iniciando proceso")
        time.sleep(1)

        # Ciclo
        with open("ban.txt", "r") as archivo:
            est_ban = archivo.read()
        while (est_ban=="0"):
            with open("estado.txt", "r") as archivo:
                estado = archivo.read()
                #print(estado)
            with open("mensaje.txt", "r") as archivo:
                mensaje = archivo.read()
                #print(mensaje)
            #print("estado= ",estado)
            barra_progreso['value'] = int(estado)
            window.update_idletasks()
            progres_label.grid(row=6, column=1, padx=10, pady=10)
            progres_label.config(text=mensaje)
            #time.sleep(1)
            with open("ban.txt", "r") as archivo:
                est_ban = archivo.read()

        # ¡Completado!
        barra_progreso['value'] = 100
        window.update_idletasks()
        time.sleep(1)
        progres_label.grid_forget()
        barra_progreso.grid_forget()
        men = "Las imágenes se han clasificado en la ruta \n"+ruta
        final_label.grid(row=5, column=1, padx=10, pady=10)
        final_label.config(text=men)


    def end():
        print("fin")
        with open("ban.txt", "w") as archivo:
            archivo.write(str("0"))
        input_entry.delete(0, 'end')
        window.destroy()
        sys.exit(0)

    def credits():
        print("by msee")

    colorr = "#7B00FF"

    # Crear ventana
    window = tk.Tk()
    window.title("Clasificador de imágenes")
    window.configure(bg=colorr)

    # Obtener el tamaño de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = int((screen_width - 866) / 2)
    y = int((screen_height - 578) / 2)

    # Establecer la posición y tamaño de la ventana
    window.geometry(f"866x578+{x}+{y}")

    # Agregar el título
    title_label = tk.Label(window, text="Clasificador de imágenes", font=("Arial", 24, "bold"), bg=colorr, fg="white")
    # title_label.pack(pady=20)
    title_label.grid(row=0, column=1, padx=10, pady=10)

    # Agregar espacios en blanco
    blank_space1 = tk.Label(window, bg=colorr)
    # blank_space1.pack()
    blank_space1.grid(row=1, column=0, padx=10, pady=10)

    # Agregar un campo de entrada (input)
    input_entry = tk.Entry(window, width=70)
    # input_entry.pack(side=tk.LEFT,padx=30, expand=tk.TRUE)
    input_entry.config(fg='gray')
    input_entry.insert(0, 'Ingrese ruta ej. C://user/images')
    input_entry.grid(row=2, column=1, padx=10, pady=10)

    # Establecer placeholder
    input_entry.bind("<Button-1>", click)

    # Agregar botón para elegir carpeta
    choose_folder_button = tk.Button(window, text="Seleccionar Carpeta", width=20, command=choose_folder,
                                     foreground="#FFFFFF", background=colorr,
                                     activeforeground="#FFFFFF", activebackground="#B879FC",
                                     overrelief="flat")
    # choose_folder_button.pack(side=tk.RIGHT, padx=30, expand=tk.TRUE)
    choose_folder_button.grid(row=2, column=3, padx=10, pady=10)

    # Agregar botón para iniciar proceso
    start_button = tk.Button(window, text="Iniciar", width=15, command=save,
                             foreground="#FFFFFF", background=colorr,
                             activeforeground="#FFFFFF", activebackground="#B879FC",
                             overrelief="flat")
    start_button.grid(row=3, column=2, padx=10, pady=10)

    # Agregar espacios en blanco
    blank_space2 = tk.Label(window, bg=colorr)
    # blank_space1.pack()
    blank_space2.grid(row=4, column=0, padx=10, pady=10)

    # Añadir barra de progreso
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("TProgressbar", foreground='white', background=colorr)
    barra_progreso = ttk.Progressbar(window, style="TProgressbar", length=300, mode="determinate")
    barra_progreso.grid(row=5, column=1, padx=10, pady=10)

    # Etiqueta para fin del proceso, aquí debería tener la ruta
    final_label = tk.Label(window, foreground="#FFFFFF", background=colorr)

    # Etiqueta para progreso
    progres_label = tk.Label(window, foreground="#FFFFFF", background=colorr)

    # Agregar espacios en blanco
    blank_space3 = tk.Label(window, bg=colorr)
    # blank_space1.pack()
    blank_space3.grid(row=6, column=0, padx=10, pady=10)

    # Agregar botón para salir y terminar ejecución
    end_button = tk.Button(window, text="x", width=2,height=2, command=end,
                             foreground="#FFFFFF", background=colorr,
                             activeforeground="#FFFFFF", activebackground="#B879FC",
                             overrelief="flat")
    end_button.grid(row=8, column=1, padx=10, pady=10)

    # Agregar botón para mostrar créditos
    cred_button = tk.Button(window, text="?", width=2, height=2, command=credits,
                           foreground="#FFFFFF", background=colorr,
                           activeforeground="#FFFFFF", activebackground="#B879FC",
                           overrelief="flat")
    cred_button.grid(row=8, column=2, padx=10, pady=10)

    window.mainloop()