import xml.etree.ElementTree as ET
from xml.dom import minidom
from Dron import Dron
from Altura import Altura
from Sistemas import Sistemas
import Listas.ListaAlturas as lista_alturas
import Listas.ListaDrones as lista_drones
import SG as sg

def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()
    
    
    for sistemaDrones in root.findall(".//sistemaDrones"):
        listaDrones = lista_drones.lista_drones().borrarTodos()     
        listaDrones= lista_drones.lista_drones()
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
                alturas = [altura.text for altura in contenido.findall(".//altura")]
                for altura in contenido.findall(".//altura"):
                    altura_obj= Altura(altura.attrib["valor"], altura.text)
                    listaAlturas.insertar(altura_obj)
                dron_obj= Dron("", dron, 0, "Espera", listaAlturas)
                listaDrones.insertar(dron_obj)
            print()
            sistema_obj= Sistemas(nombre, alturaMaxima, cantidadDrones, listaDrones)
            sg.list.insertar(sistema_obj)
        

    for mensaje in root.findall(".//Mensaje"):
        nombre = mensaje.get("nombre")
        sistemaDrones = mensaje.find("sistemaDrones").text
        instrucciones = [instruccion.text for instruccion in mensaje.findall(".//instruccion")]
        print(f"Mensaje: {nombre}")
        print(f"Sistema de Drones: {sistemaDrones}")
        print(f"Instrucciones: {', '.join(instrucciones)}")
        print()


