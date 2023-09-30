import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
import Logic as logic
import subprocess
import os
from PIL import Image, ImageTk
import SG as sg
from tkinter import ttk 

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador")
        self.path = None
        self.conteo_linea = 1

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.linea_numero = tk.Text(self.root, width=2, padx=2, takefocus=0, border=0, background='black', state='disabled')
        self.linea_numero.pack(side=tk.LEFT, fill=tk.Y)
        self.linea_numero.config(fg='white')
        self.widget = ScrolledText(self.root, wrap=tk.WORD, width=100, height=20)
        self.widget.pack(expand=True, fill='both')

        self.widget.bind('<Key>', self.actualizar_linea_num)
        self.widget.bind('<MouseWheel>', self.actualizar_linea_num)
    
    def create_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Inicializar", command=self.inicializar)
        menu_bar.add_cascade(label="Cargar Archivo XML", command=self.open_file)
        menu_bar.add_cascade(label="Generar Archivo XML", command=self.generarArchivoSalida)
        
        menu_bar.add_cascade(label="Gestion de drones", menu=file_menu)
        file_menu.add_command(label="Ver listado de drones", command=self.ver_listado_drones)
        file_menu.add_command(label="Agregar un nuevo dron", command=self.open_file)
        file_menu.add_command(label="Guardar listado de drones TXT", command=self.guardar_listado)
        
        action_menu2 = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Gestion de sistemas de drones", menu=action_menu2)
        action_menu2.add_command(label="Listado de sistemas", command=self.generar_listadoSistemas)
        action_menu2.add_command(label="Listado de drones por sistema", command=self.seleccionar_listadoDrones_Sistema)
        action_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Gestion de mensajes", menu=action_menu)
        action_menu.add_command(label="Ver listado de mensajes", command=self.ver_listado_mensajes)
        action_menu.add_command(label="Ver instrucciones para enviar un mensaje", command=self.seleccionar_Instrucciones_mensaje)
        file_menu.add_command(label="Guardar listado de mensajes TXT", command=self.guardar_listado)


        menu_bar.add_cascade(label="Ayuda")

    #funcion que inicializa el sistema es decir que limpia todas las litas
    def inicializar(self):
        sg.listDrones = sg.listaDrones.lista_drones()
        sg.list = sg.lista.lista_sistemas()
        sg.listMensajes = sg.listaMensajes.lista_Mensajes()

        self.widget.delete(1.0, tk.END)
        self.widget.insert(tk.END, "Se inicializo el sistema ")
    #generar archivo de salida
    def generarArchivoSalida(self):
        logic.generarArchivoSalida()
        self.widget.delete(1.0, tk.END)
        self.widget.insert(tk.END, "Se genero el archivo de salida ")

    def actualizar_linea_num(self, event=None):
        conteo = self.widget.get('1.0', tk.END).count('\n')
        if conteo != self.conteo_linea:
            self.linea_numero.config(state=tk.NORMAL)
            self.linea_numero.delete(1.0, tk.END)
            for line in range(1, conteo + 1):
                self.linea_numero.insert(tk.END, f"{line}\n")
            self.linea_numero.config(state=tk.DISABLED)
            self.conteo_linea = conteo
    
    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
        if path:
            logic.leerEntrada(path)
            self.widget.delete(1.0, tk.END)
            self.widget.insert(tk.END, "Se cargo correctamente el archivo de la ruta: " + path)
        else:
            messagebox.showerror("Error", "Archivo no válido")

    ##ver listado de drones y lo muestra en el widget
    def ver_listado_drones(self):
        if sg.listDrones != None:
            self.widget.delete(1.0, tk.END)
            self.widget.insert(tk.END, sg.listDrones.recorrer())
            #actualizar lineas
            self.actualizar_linea_num()
        else:
            messagebox.showerror("Error", "No se ha cargado un archivo XML")

    #Guardar listado de drones como TXT
    def guardar_listado(self):
        path = filedialog.asksaveasfilename(filetypes=[("Archivos TXT", "*.txt")])
        if path:
            with open(path, "w") as file:
                text = self.widget.get(1.0, tk.END)
                file.write(text)
            self.path = path
        else:
            messagebox.showerror("Error", "Archivo no válido")
    
    #Generar una ventana externa que muestre una imagen
    def generar_listadoSistemas(self):
        if sg.list !=None:
            sg.list.generarGraficaSistemas()    
            archivo = "graficas/Sistemas.png"
            self.mostrar_imagen(archivo)
        else:
            messagebox.showerror("Error", "No se ha cargado un archivo XML")


    ##funcion para ver listado de mnesajes
    def ver_listado_mensajes(self):
        if sg.list !=None:
            self.widget.delete(1.0, tk.END)
            self.widget.insert(tk.END, sg.listMensajes.obtenerMensajes())
            #actualizar lineas
            self.actualizar_linea_num()
        else:
            messagebox.showerror("Error", "No se ha cargado un archivo XML")
    
    def seleccionar_listadoDrones_Sistema(self):
        if sg.list !=None:
            sg.list.generarGrafica()
            def seleccionar_opcion():
                seleccion = combo.get()  # Obtiene la opción seleccionada
                messagebox.showinfo("Selección", f"Has seleccionado: {seleccion}")
                archivo = "graficas/"+ seleccion + ".png"
                self.mostrar_imagen(archivo)
                ventana_combobox.destroy()  # Cierra la ventana emergente


            # Crea una ventana emergente
            ventana_combobox = Toplevel(self.root)
            ventana_combobox.title("Seleccionar Opción")

            # Crea un Combobox con opciones múltiples
            opciones = sg.list.obtenerListadoSistemas()
            combo = ttk.Combobox(ventana_combobox, values=opciones, state="readonly")
            combo.pack(pady=10)

            # Crea un botón para aceptar la selección
            boton_aceptar = Button(ventana_combobox, text="Aceptar", command=seleccionar_opcion)
            boton_aceptar.pack()
        else:
            messagebox.showerror("Error", "No se ha cargado un archivo XML")

        #seleccionar instrucciones para enviar un mensaje
            
    def seleccionar_Instrucciones_mensaje(self):
        if sg.listMensajes !=None:
            sg.listMensajes.generarGrafica()
            def seleccionar_opcion():
                seleccion = combo.get()  # Obtiene la opción seleccionada
                messagebox.showinfo("Selección", f"Has seleccionado: {seleccion}")
                archivo = "graficas/"+ seleccion + ".png"
                self.mostrar_imagen(archivo)
                ventana_combobox.destroy()  # Cierra la ventana emergente


            # Crea una ventana emergente
            ventana_combobox = Toplevel(self.root)
            ventana_combobox.title("Seleccionar Opción")

            # Crea un Combobox con opciones múltiples
            opciones = sg.listMensajes.obtenerListadoMensajes()
            combo = ttk.Combobox(ventana_combobox, values=opciones, state="readonly")
            combo.pack(pady=10)

            # Crea un botón para aceptar la selección
            boton_aceptar = Button(ventana_combobox, text="Aceptar", command=seleccionar_opcion)
            boton_aceptar.pack()
        else:
            messagebox.showerror("Error", "No se encontraron mensajes")




    def mostrar_imagen(self, pathImg):
        # Obtén el directorio actual del script (donde se encuentra este archivo .py)

        script_directory = os.path.dirname(os.path.abspath(__file__))
    # Nombre del archivo que deseas obtener (en este caso, "msg.png")
        archivo = pathImg

    # Construye la ruta completa al archivo
        ruta_completa = os.path.join(script_directory, archivo)

        if os.name == 'nt':  # Verifica si el sistema operativo es Windows
            try:
                # Intenta abrir la imagen con el visor de imágenes predeterminado de Windows
                os.startfile(ruta_completa)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir la imagen: {str(e)}")
        else:
            try:
                # Intenta abrir la imagen con el programa predeterminado en sistemas no Windows
                subprocess.Popen(['xdg-open', ruta_completa])  # En sistemas basados en Linux
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir la imagen: {str(e)}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
