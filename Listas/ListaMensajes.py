from Mensaje import Mensaje


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
    
    def borrarTodos(self):
        self.primero = None