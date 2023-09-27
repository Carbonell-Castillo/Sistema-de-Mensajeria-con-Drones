import xml.etree.ElementTree as ET
from xml.dom import minidom
from Dron import Dron
from Altura import Altura
from Sistemas import Sistemas
from Instruccion import Instruccion
from Mensaje import Mensaje
import Listas.ListaAlturas as lista_alturas
import Listas.ListaDrones as lista_drones
import Listas.ListaInstrucciones as lista_instrucciones
import SG as sg


def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()
    generarListaDrones(xml_file)
    
    

    for sistemaDrones in root.findall(".//sistemaDrones"):
        listaDrones = lista_drones.lista_drones().borrarTodos()     
        listaDrones= lista_drones.lista_drones()
        if sg.list != None:
            if sg.list.validarNombre(sistemaDrones.get("nombre")):
                print("Sistema ya existe")
                print()
                continue
        nombre = sistemaDrones.get("nombre")
        alturaMaxima_elem = sistemaDrones.find("alturaMaxima")
        cantidadDrones_elem = sistemaDrones.find("cantidadDrones")
        
        if alturaMaxima_elem is not None and cantidadDrones_elem is not None:
            alturaMaxima = sistemaDrones.find("alturaMaxima").text
            cantidadDrones = sistemaDrones.find("cantidadDrones").text
        
            for contenido in sistemaDrones.findall("contenido"):
                listaAlturas= lista_alturas.lista_Alturas().borrarTodos()
                listaAlturas = lista_alturas.lista_Alturas()
                dron = contenido.find("dron").text
                if sg.listDrones.validarNombre(dron):
                    for altura in contenido.findall(".//altura"):
                        #Se valida que el valor de la altura sea menor o igual que la altura mayor
                        if int(altura.attrib["valor"]) <= int(alturaMaxima):
                            ##valida que la altura no sea "" en caso contrario que agregue " "
                            if altura.text == "":
                                altura_text=" "
                            else:
                                altura_text= altura.text
                            
                            altura_obj= Altura(altura.attrib["valor"], altura_text)
                            listaAlturas.insertar(altura_obj)
                        else:
                            print("La altura excede la altura maxima del sistema")
                                        
                    dron_obj= Dron("", dron, 0, "Espera", listaAlturas)
                    listaDrones.insertar(dron_obj)
                else:
                    print("Dron no encontrado")
                    print()
            print()
            sistema_obj= Sistemas(nombre, alturaMaxima, cantidadDrones, listaDrones)
            sg.list.insertar(sistema_obj)

            
    
    for mensaje in root.findall(".//Mensaje"):
        listaInstrucciones= lista_instrucciones.lista_Instrucciones().borrarTodos()
        listaInstrucciones= lista_instrucciones.lista_Instrucciones()
        nombre = mensaje.get("nombre")
        sistemaDrones = mensaje.find("sistemaDrones").text
        instrucciones = [instruccion.text for instruccion in mensaje.findall(".//instruccion")]
        mensaje_resultado =""
        for instruccion in mensaje.findall(".//instruccion"):
            dron = instruccion.attrib["dron"]

            altura = instruccion.text
            contador_tiempo=1
            letraEncontrada= sg.list.instruccionDron(sistemaDrones, dron, altura)
            alturaInicialDron= int(sg.list.obtenerAlturaInicial(sistemaDrones, dron))
            print("atura inical  ", alturaInicialDron)
            ##Se comienzan a crear las instruciones
            if int(altura)> alturaInicialDron:
                for altura in range(alturaInicialDron, int(altura)):
                    alturaInicialDron= alturaInicialDron+1
                    instruccion_obj = Instruccion(contador_tiempo, dron, "Subir")
                    sg.list.actualizarAltura(sistemaDrones, dron, alturaInicialDron)
                    contador_tiempo= contador_tiempo+1
                    listaInstrucciones.insertar(instruccion_obj)
                instruccion_obj = Instruccion(contador_tiempo, dron, "Emitir Luz")
                listaInstrucciones.insertar(instruccion_obj)
            elif int(altura)< alturaInicialDron:
                contador_tiempo = listaInstrucciones.obtenerUltimoDron(dron)
                print("contador tiempo 2 ", contador_tiempo)
                contador_tiempo= contador_tiempo+1

                for altura in range(alturaInicialDron, int(altura), -1):
                    alturaInicialDron= alturaInicialDron-1
                    instruccion_obj = Instruccion(contador_tiempo, dron, "Bajar")
                    sg.list.actualizarAltura(sistemaDrones, dron, alturaInicialDron)                    
                    contador_tiempo= contador_tiempo+1
                    listaInstrucciones.insertar(instruccion_obj)
                instruccion_obj = Instruccion(contador_tiempo, dron, "Encender Luz")
                listaInstrucciones.insertar(instruccion_obj)

            cantidadDrones = int(sg.list.obtenerCantidadDrones(sistemaDrones))

            tiempo_mayor= int(listaInstrucciones.obtenerTiempoMayor())

        ##llnar los drones restantes
        for i in range(0, cantidadDrones):
            nombre_dron_encontrado = sg.list.obtenerDronIndice(sistemaDrones, i)
            print("Dron encontrado: ", nombre_dron_encontrado)
            ultimo_tiempo_dron = int(listaInstrucciones.obtenerUltimoDron(nombre_dron_encontrado))
            
            if ultimo_tiempo_dron < tiempo_mayor:
                for j in range(ultimo_tiempo_dron+1, tiempo_mayor+1):
                    ultimo_tiempo_dron = ultimo_tiempo_dron+1
                    instruccion_obj = Instruccion(ultimo_tiempo_dron, nombre_dron_encontrado, "Espera")
                    listaInstrucciones.insertar(instruccion_obj)
                    
            mensaje_resultado =mensaje_resultado+str(letraEncontrada)
            print("Letra: ", letraEncontrada)
        mensaje_obj = Mensaje(nombre, sistemaDrones, listaInstrucciones)
        sg.listMensajes.insertar(mensaje_obj)
        print(f"Mensaje: {nombre}")
        print(f"SistemaDrones: {sistemaDrones}")
        print(f"Mensaje final: {mensaje_resultado}")
        print(f"Sistema de Drones: {sistemaDrones}")
        print(f"Instrucciones: {', '.join(instrucciones)}")
        print()

def generarListaDrones(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()
    for child in root:
        if child.tag == "listaDrones":
            for dron in child:
                if sg.listDrones is not None:
                    if sg.listDrones.validarNombre(dron.text):
                        print("Dron ya existe")
                        print()
                    else:
                        dron_obj = Dron("", dron.text, 0, "Espera", None)
                        sg.listDrones.insertar(dron_obj)
                else:
                    dron_obj = Dron("", dron.text, 0, "Espera", None)
                    sg.listDrones.insertar(dron_obj)
                print(dron.text)


