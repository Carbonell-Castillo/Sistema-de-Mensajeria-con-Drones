import tkinter as tk
from tkinter import filedialog
from Listas.ListaSistemas import lista_sistemas
import SG as sg ##Super global
import Logic as logic


if __name__ == "__main__":
    
    while True:
        option = sg.showMenu()

        if option == 1:
            archivo_entrada = sg.open_file()        
            if archivo_entrada:
                print("Cargando archivo de entrada desde:", archivo_entrada)
                logic.leerEntrada(archivo_entrada)

        elif option == 2:
            print("Comienza a mostrar todo")    
            print("")
            
            sg.list.recorrer()
        
        elif option ==3:
            print("Comienza a mostrar todo")    
            print("")
            sg.listMensajes.recorrer()
        elif option ==4:
            print("Comienza a escribir salida")    
            print("")
            logic.generarArchivoSalida()
        elif option ==5:
            print("Comienza a generar todas las graficas salida")    
            print("")
            sg.list.generarGrafica()
            
        elif option ==6:
            print("Comienza a generar graficas por nombre de sistema")    
            print("")
            sg.list.generarGraficaSistema("ADF")
        elif option ==7:
            print("Comienza a generar graficas por nombre de sistema")    
            print("")
            sg.listMensajes.generarGrafica()
        elif option ==9:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")