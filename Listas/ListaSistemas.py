
##importar el Sistemas que se encuentra en ../Sistemas.py
from Sistemas import Sistemas
from Arbol import *

class nodo:
    def __init__(self, Sistemas=None, siguiente=None):
        self.Sistemas = Sistemas
        self.siguiente = siguiente


class lista_sistemas:
    def __init__(self):
        self.primero = None

    def insertar(self, Sistemas):
        if self.primero is None:
            self.primero = nodo(Sistemas=Sistemas)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(Sistemas=Sistemas)

    def recorrer(self):
        actual = self.primero
        print("-----Sistemas------: \n")
        print(
            "----------------------------------------------------------------------------"
        )
        while actual != None:
            print(
                "Nombre: ",
                actual.Sistemas._nombre,
                " AlturaMaxima: ",
                actual.Sistemas._alturaMaxima,
                " Cantidad Drones: ",
                actual.Sistemas._cantidadDrones,
            )
            actual.Sistemas._listadoDrones.recorrer()
            actual = actual.siguiente

            
        print(
            "----------------------------------------------------------------------------"
        )

    def buscar(self, nombre, listAlturas):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombre:
                actual.Sistemas._listadoAlturas=listAlturas
            actual = actual.siguiente
    
    def validarNombre(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    

    def obtenerCantidadDrones(self, nombreSistema):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombreSistema:
                return actual.Sistemas._listadoDrones.obtenerCantidadDrones()
            actual = actual.siguiente
        return 0
    
    ##obtener dron por indice
    def obtenerDronIndice(self, nombreSistema, indice):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombreSistema:
                return actual.Sistemas._listadoDrones.obtenerDronPorIndice(indice)
            actual = actual.siguiente
        return "Nop"
    
    
    def borrarTodos(self):
        self.primero = None

    def instruccionDron(self, nombreSistema, nombreDron, altura):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombreSistema:
                return actual.Sistemas._listadoDrones.instruccion(nombreDron, altura)
            actual = actual.siguiente
        return "No se encontro el sistema"

    ##obtener altura inicial dron
    def obtenerAlturaInicial(self, nombreSistema, nombreDron):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombreSistema:
                return actual.Sistemas._listadoDrones.obtenerAlturaInicial(nombreDron)
            actual = actual.siguiente
        return "No se encontro el sistema"
    
    ##actualizar altura
    def actualizarAltura(self, nombreSistema, nombreDron, altura):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombreSistema:
                return actual.Sistemas._listadoDrones.actualizarAltura(nombreDron, altura)
            actual = actual.siguiente
        return "No se encontro el sistema"

    ##funcion generarGrafica
    def generarGrafica(self):
        actual = self.primero
        while actual != None:
            arbol.dot.clear()
            raiz= arbol.agregarNodo(actual.Sistemas._nombre)
            cantidadDrones = actual.Sistemas._listadoDrones.obtenerCantidadDrones()
            for i in range(cantidadDrones):
                actual.Sistemas._listadoDrones.ordenarDrones()
                arbol.agregarArista(raiz, actual.Sistemas._listadoDrones.obtenerDronPorIndice(i))
            arbol.generarGrafica(actual.Sistemas._nombre, "png")
            actual = actual.siguiente
    
    ##generar grafica por sistema
    def generarGraficaSistema(self, nombreSistema):
        actual = self.primero
        while actual != None:
            if actual.Sistemas._nombre == nombreSistema:
                arbol.dot.clear()
                raiz= arbol.agregarNodo(actual.Sistemas._nombre)
                cantidadDrones = actual.Sistemas._listadoDrones.obtenerCantidadDrones()
                for i in range(cantidadDrones):
                    actual.Sistemas._listadoDrones.ordenarDrones()
                    arbol.agregarArista(raiz, actual.Sistemas._listadoDrones.obtenerDronPorIndice(i))
                arbol.generarGrafica(actual.Sistemas._nombre, "png")
            actual = actual.siguiente