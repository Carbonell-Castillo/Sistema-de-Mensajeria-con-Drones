from Mensaje import Mensaje
from Arbol import *

class nodo:
    def __init__(self, Mensaje=None, siguiente=None):
        self.Mensaje = Mensaje
        self.siguiente = siguiente


class lista_Mensajes:
    def __init__(self):
        self.primero = None

    def insertar(self, Mensaje):
        if self.primero is None:
            self.primero = nodo(Mensaje=Mensaje)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(Mensaje=Mensaje)

    def recorrer(self):
        actual = self.primero
        print("Mensajes: \n")
        print(
            "----------------------------------------------------------------------------"
        )
        while actual != None:
            print(
                " Nombre: ",
                actual.Mensaje._nombre,
                " nombre Sistemas drones: ",
                actual.Mensaje._nombreSistemaDrones,
                " tiempo optimo: ",
                actual.Mensaje._tiempoOptimo,
                " mensaje recibido: ",
                actual.Mensaje._mensajeRecibido
            )
            if actual.Mensaje._instrucciones != None:
                actual.Mensaje._instrucciones.ordenar()
                actual.Mensaje._instrucciones.recorrer()
            actual = actual.siguiente
        print(
            "----------------------------------------------------------------------------"
        )


    def validarNombre(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.Mensaje._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    #obtenerCantidadMensajes
    def obtenerCantidadMensajes(self):
        actual = self.primero
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente
        return contador

    #obtenerMensajeIndice
    def obtenerMensajeIndice(self, indice):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice:
                return actual.Mensaje
            contador = contador + 1
            actual = actual.siguiente
        return None

    ##graficar instrucciones
    def generarGrafica(self):
        actual = self.primero

        while actual != None:
            arbol.dot.clear()
            raiz1 = arbol.agregarNodo(actual.Mensaje._nombre)
            raiz2 = arbol.agregarNodo(f"Mensaje Recibido: \\n{actual.Mensaje._mensajeRecibido}")
            raiz3=arbol.agregarNodo(f"Tiempo optimo: {actual.Mensaje._tiempoOptimo}")
            arbol.agregarArista(raiz1, raiz2)
            arbol.agregarArista(raiz2, raiz3)

            cantidadInstrucciones = actual.Mensaje._instrucciones.obtenerCantidadInstrucciones()
            tiempoOptimo = actual.Mensaje._tiempoOptimo
            contador_tiempo = 0
            nodoAntes =None
            nodoAntesEstado=None
            nodoTiempoAnterior = None
            instruccionGeneral = None
            for i in range(0, tiempoOptimo):
                tiempo_obtener = i+1
                listaInstruccionesTiempo = actual.Mensaje._instrucciones.obtenerInstruccionesTiempo(tiempo_obtener)
                listaInstruccionesTiempo.ordenar()
                cantidadInstrucciones = listaInstruccionesTiempo.obtenerCantidadInstrucciones()
                if listaInstruccionesTiempo != None:
                    for j in range(0, cantidadInstrucciones):
                        instruccion = listaInstruccionesTiempo.obtenerInstruccionIndiceSolo(j)
                        if i==0:
                            nodoDron = arbol.agregarNodo(f"{instruccion._nombreDron}")
                            arbol.agregarArista(raiz2, nodoDron)
                            nodoAntes = nodoDron
                            cantidadInstruccionesTotal = actual.Mensaje._instrucciones.obtenerCantidadInstrucciones()
                            contadorI=0
                            for k in range(0, cantidadInstruccionesTotal):
                                instruccionGeneral = actual.Mensaje._instrucciones.obtenerInstruccionIndiceSolo(k)
                                if instruccionGeneral._nombreDron == instruccion._nombreDron:
                                    contadorI=contadorI+1
                                    if contadorI ==1:
                                        print("Se agrego el primero")
                                        nodoEstado = arbol.agregarNodo(f"{instruccionGeneral._estado}")
                                        arbol.agregarArista(nodoAntes, nodoEstado)
                                        nodoAntesEstado = nodoEstado
                                    else:
                                        nodoEstado = arbol.agregarNodo(f"{instruccionGeneral._estado}")
                                        arbol.agregarArista(nodoAntesEstado, nodoEstado)
                                        nodoAntesEstado = nodoEstado
                
                if i==0:
                    nodoTiempo = arbol.agregarNodo(f"Tiempo: {tiempo_obtener}")
                    arbol.agregarArista(raiz3, nodoTiempo)
                    nodoTiempoAnterior = nodoTiempo
                else:
                    nodoTiempo = arbol.agregarNodo(f"Tiempo: {tiempo_obtener}")
                    arbol.agregarArista(nodoTiempoAnterior, nodoTiempo)
                    nodoTiempoAnterior = nodoTiempo
            arbol.generarGrafica(actual.Mensaje._nombre, "png")
            actual = actual.siguiente
    def borrarTodos(self):
        self.primero = None

    #generar grafica nombre mensaje
    def generarGraficaNombreMensaje(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.Mensaje._nombre == nombre:
                arbol.dot.clear()
                raiz1 = arbol.agregarNodo(actual.Mensaje._nombre)
                raiz2 = arbol.agregarNodo(f"Mensaje Recibido: \\n{actual.Mensaje._mensajeRecibido}")
                raiz3=arbol.agregarNodo(f"Tiempo optimo: {actual.Mensaje._tiempoOptimo}")
                arbol.agregarArista(raiz1, raiz2)
                arbol.agregarArista(raiz2, raiz3)

                cantidadInstrucciones = actual.Mensaje._instrucciones.obtenerCantidadInstrucciones()
                tiempoOptimo = actual.Mensaje._tiempoOptimo
                contador_tiempo = 0
                nodoAntes =None
                nodoAntesEstado=None
                nodoTiempoAnterior = None
                instruccionGeneral = None
                for i in range(0, tiempoOptimo):
                    tiempo_obtener = i+1
                    listaInstruccionesTiempo = actual.Mensaje._instrucciones.obtenerInstruccionesTiempo(tiempo_obtener)
                    listaInstruccionesTiempo.ordenar()
                    cantidadInstrucciones = listaInstruccionesTiempo.obtenerCantidadInstrucciones()
                    if listaInstruccionesTiempo != None:
                        for j in range(0, cantidadInstrucciones):
                            instruccion = listaInstruccionesTiempo.obtenerInstruccionIndiceSolo(j)
                            if i==0:
                                nodoDron = arbol.agregarNodo(f"{instruccion._nombreDron}")
                                arbol.agregarArista(raiz2, nodoDron)
                                nodoAntes = nodoDron
                                cantidadInstruccionesTotal = actual.Mensaje._instrucciones.obtenerCantidadInstrucciones()
                                contadorI=0
                                for k in range(0, cantidadInstruccionesTotal):
                                    instruccionGeneral = actual.Mensaje._instrucciones.obtenerInstruccionIndiceSolo(k)
                                    if instruccionGeneral._nombreDron == instruccion._nombreDron:
                                        contadorI=contadorI+1
                                        if contadorI ==1:
                                            print("Se agrego el primero")
                                            nodoEstado = arbol.agregarNodo(f"{instruccionGeneral._estado}")
                                            arbol.agregarArista(nodoAntes, nodoEstado)
                                            nodoAntesEstado = nodoEstado
                                        else:
                                            nodoEstado = arbol.agregarNodo(f"{instruccionGeneral._estado}")
                                            arbol.agregarArista(nodoAntesEstado, nodoEstado)
                                            nodoAntesEstado = nodoEstado
                
                    if i==0:
                        nodoTiempo = arbol.agregarNodo(f"Tiempo: {tiempo_obtener}")
                        arbol.agregarArista(raiz3, nodoTiempo)
                        nodoTiempoAnterior = nodoTiempo
                    else:
                        nodoTiempo = arbol.agregarNodo(f"Tiempo: {tiempo_obtener}")
                        arbol.agregarArista(nodoTiempoAnterior, nodoTiempo)
                        nodoTiempoAnterior = nodoTiempo
                    arbol.generarGrafica(actual.Mensaje._nombre, "png")
            actual = actual.siguiente
