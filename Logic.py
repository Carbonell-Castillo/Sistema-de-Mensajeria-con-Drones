import xml.etree.ElementTree as ET
from xml.dom import minidom
from Dron import Dron
from Altura import Altura
from Sistemas import Sistemas
import Listas.ListaAlturas as lista_alturas
import Listas.ListaDrones as lista_drones
import SG as sg
listaDrones= lista_drones.lista_drones()

def leerEntrada(xml_file):
    global listaDrones
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()
    generarListaDrones(xml_file)
    
    
    
    for sistemaDrones in root.findall(".//sistemaDrones"):
        
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
                if listaDrones.validarNombre(dron):
                    for altura in contenido.findall(".//altura"):
                        altura_obj= Altura(altura.attrib["valor"], altura.text)
                        listaAlturas.insertar(altura_obj)
                    
                    
                    print("Dron---")
                    print(dron)
                    listaDrones.cambiarListAlturas(dron, listaAlturas)
                else:
                    print("Dron no encontrado")
                    print()
            print()
            sistema_obj= Sistemas(nombre, alturaMaxima, cantidadDrones, listaDrones)
            sg.list.insertar(sistema_obj)
            listaDrones= lista_drones.lista_drones().borrarTodos
            generarListaDrones(xml_file)

            

    for mensaje in root.findall(".//Mensaje"):
        nombre = mensaje.get("nombre")
        sistemaDrones = mensaje.find("sistemaDrones").text
        instrucciones = [instruccion.text for instruccion in mensaje.findall(".//instruccion")]
        print(f"Mensaje: {nombre}")
        print(f"Sistema de Drones: {sistemaDrones}")
        print(f"Instrucciones: {', '.join(instrucciones)}")
        print()

def generarListaDrones(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()
    global listaDrones
    listaDrones= lista_drones.lista_drones()
    for child in root:
        if child.tag == "listaDrones":
            for dron in child:
                if listaDrones is not None:
                    if listaDrones.validarNombre(dron.text):
                        print("Dron ya existe")
                        print()
                    else:
                        dron_obj = Dron("", dron.text, 0, "Espera", None)
                        listaDrones.insertar(dron_obj)
                else:
                    dron_obj = Dron("", dron.text, 0, "Espera", None)
                    listaDrones.insertar(dron_obj)
                print(dron.text)


