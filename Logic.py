import xml.etree.ElementTree as ET
from xml.dom import minidom
from Dron import Dron
from Altura import Altura
import Listas.ListaAlturas as lista_alturas
import Listas.ListaDrones as lista_drones
from Listas.ListaSistemas import lista_sistemas
def validar_tiempo_amplitud(tiempo, amplitud, signal_t, signal_a):
    if tiempo < 1 or tiempo > signal_t:
        raise ValueError(f"Valor de tiempo inválido en dato: {tiempo}")
    if amplitud < 1 or amplitud > signal_a:
        raise ValueError(f"Valor de amplitud inválido en dato: {amplitud}")
        

def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()

    # obtener la lectura de estos datos 
#     <?xml version="1.0" encoding="UTF-8"?>
# <config>
#    <listaDrones>
#       <dron>DronY</dron>
#       <dron>DronX</dron>
#       <dron>DronW</dron>
#       <dron>DronZ</dron>
#       <dron>DronA</dron>
#    </listaDrones>
#    <listaSistemasDrones>
#       <sistemaDrones nombre="SD1">
#          <alturaMaxima>7</alturaMaxima>
#          <cantidadDrones>3</cantidadDrones>
#          <contenido>
#             <dron>DronX</dron>
#             <alturas>
#                <altura valor="1">A</altura>
#                <altura valor="2">I</altura>
#                <altura valor="3">D</altura>
#                <altura valor="4">F</altura>
#                <altura valor="5">I</altura>
#                <altura valor="6">J</altura>
#                <altura valor="7">K</altura>
#             </alturas>
#          </contenido>
#          <contenido>
#             <dron>DronY</dron>
#             <alturas>
#                <altura valor="1">2</altura>
#                <altura valor="2">C</altura>
#                <altura valor="3">P</altura>
#                <altura valor="4">G</altura>
#                <altura valor="5">L</altura>
#                <altura valor="6">M</altura>
#                <altura valor="7">N</altura>
#             </alturas>
#          </contenido>
#          <contenido>
#             <dron>DronZ</dron>
#             <alturas>
#                <altura valor="1">B</altura>
#                <altura valor="2">C</altura>
#                <altura valor="3">E</altura>
#                <altura valor="4">H</altura>
#                <altura valor="5">O</altura>
#                <altura valor="6">P</altura>
#                <altura valor="7">Q</altura>
#             </alturas>
#          </contenido>
#       </sistemaDrones>
#       <sistemaDrones nombre="SDF">
#          <alturaMaxima>1</alturaMaxima>
#          <cantidadDrones>4</cantidadDrones>
#          <contenido>
#             <dron>DronW</dron>
#             <alturas>
#                <altura valor="1">I</altura>
#             </alturas>
#          </contenido>
#          <contenido>
#             <dron>DronX</dron>
#             <alturas>
#                <altura valor="1">P</altura>
#             </alturas>
#          </contenido>
#          <contenido>
#             <dron>DronY</dron>
#             <alturas>
#                <altura valor="1">C</altura>
#             </alturas>
#          </contenido>
#          <contenido>
#             <dron>DronZ</dron>
#             <alturas>
#                <altura valor="1">2</altura>
#             </alturas>
#          </contenido>
#       </sistemaDrones>
#    </listaSistemasDrones>
#    <listaMensajes>
#       <Mensaje nombre="msg">
#          <sistemaDrones>SD1</sistemaDrones>
#          <instrucciones>
#             <instruccion dron="DronX">2</instruccion>
#             <instruccion dron="DronY">3</instruccion>
#             <instruccion dron="DronZ">2</instruccion>
#             <instruccion dron="DronY">1</instruccion>
#          </instrucciones>
#       </Mensaje>
#       <Mensaje nombre="msg2">
#          <sistemaDrones>SDF</sistemaDrones>
#          <instrucciones>
#             <instruccion dron="DronW">1</instruccion>
#             <instruccion dron="DronX">1</instruccion>
#             <instruccion dron="DronY">1</instruccion>
#             <instruccion dron="DronZ">1</instruccion>
#          </instrucciones>
#       </Mensaje>
#    </listaMensajes>
# </config>
    for child in root:
        listaAlturas = lista_alturas.ListaAlturas()
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
        
