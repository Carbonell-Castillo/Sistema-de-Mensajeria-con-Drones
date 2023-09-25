import tkinter as tk 
from tkinter import filedialog 
import Listas.ListaSistemas as lista

list = lista.lista_sistemas()


def showMenu():
    while True:
        print("-------------------------------------------------")
        print("Proyecto No 1 IPC 2")
        print("-------------------------------------------------")
        print("# Menu Principal\n")
        print("1. Cargar archivo")
        print("2. Ver sistemas")
        print("3. Salida\n")

        try:
            option = int(input("Ingrese una opción: "))
            if 1 <= option <= 7:
                return option
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")


def open_file():
    global rutaArchivo
    ventana = tk.Tk()
    ventana.withdraw()

    # Definir los tipos de archivo permitidos (por ejemplo, solo archivos CSV y TXT)
    tipos_archivo_permitidos = [("Archivos para leer", "*.xml"), ("Archivos de Movimientos", "*.mov")]

    # Abrir la ventana de selección de archivo con los tipos de archivo permitidos
    ruta_archivo = filedialog.askopenfilename(filetypes=tipos_archivo_permitidos)
    rutaArchivo= ruta_archivo
    # Mostrar la ruta del archivo seleccionado (esto es opcional)
    if ruta_archivo:
        print("Archivo seleccionado:", ruta_archivo)
        return ruta_archivo
    else:
        print("Ningún archivo seleccionado")
        return None