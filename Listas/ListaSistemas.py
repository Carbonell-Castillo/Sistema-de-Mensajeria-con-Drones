
from Sistemas import Sistemas


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
    
    def borrarTodos(self):
        self.primero = None