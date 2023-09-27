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

    def borrarTodos(self):
        self.primero = None