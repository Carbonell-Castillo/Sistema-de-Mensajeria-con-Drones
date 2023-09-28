import tkinter as tk 
from tkinter import filedialog 
import Listas.ListaSistemas as lista
import Listas.ListaDrones as listaDrones
import Listas.ListaMensajes as listaMensajes
list = lista.lista_sistemas()
listDrones= listaDrones.lista_drones()
listMensajes= listaMensajes.lista_Mensajes()

def showMenu():
    while True:
        print("-------------------------------------------------")
        print("Proyecto No 1 IPC 2")
        print("-------------------------------------------------")
        print("# Menu Principal\n")
        print("1. Cargar archivo")
        print("2. Ver sistemas")
        print("3. Ver mensajes")
        print("4. Archivo salida")
        print("5. Generar todas las graficas sistemas")
        print("6. seleccionar graficas sistemas")
        print("7. Generar todas las graficas mensajes")
        print("8. seleccionar graficas mensajes")
        print("9. Salida\n")

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