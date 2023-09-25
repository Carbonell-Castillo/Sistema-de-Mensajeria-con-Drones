import xml.etree.ElementTree as ET
from xml.dom import minidom
from Dron import Dron
from Altura import Altura
import Listas.ListaAlturas as lista_alturas
import Listas.ListaDrones as lista_drones
from Listas.ListaSistemas import lista_sistemas


def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()

    for child in root:
        listaAlturas = lista_alturas.lista_Alturas()
        listaDrones = lista_drones.lista_drones()
        if child.tag == "listaDrones":
            for dron in child:
                dron_obj = Dron("", dron.text, 0, "Espera", listaAlturas)
                listaDrones.insertar(dron_obj)
                print(dron.text)
        elif child.tag == "listaSistemasDrones":
            for sistema in child:
                print(sistema.attrib["nombre"])
                for contenido in sistema:
                    print(contenido.find("dron").text)
                    for altura in contenido.find("alturas"):
                        altura_obj= Altura(altura.attrib["valor"], altura.text)
                        print(sistema.attrib["valor"])
                        print(altura.text)
                        listaAlturas.insertar(altura_obj)
                    listaDrones.cambiarListAlturas(contenido.find("dron").text, listaAlturas)
                lista_sistemas.insertar(sistema.attrib["nombre"], sistema.find("alturaMaxima").text, sistema.find("cantidadDrones").text, listaDrones)
                

        elif child.tag == "listaMensajes":
            for mensaje in child:
                print(mensaje.attrib["nombre"])
                print(mensaje.find("sistemaDrones").text)
                for instruccion in mensaje.find("instrucciones"):
                    print(instruccion.attrib["dron"])
                    print(instruccion.text)
        else:
            raise ValueError(f"Etiqueta inválida: {child.tag}")
        
