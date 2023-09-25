from Dron import Dron


class nodo:
    def __init__(self, Dron=None, siguiente=None):
        self.Dron = Dron
        self.siguiente = siguiente


class lista_drones:
    def __init__(self):
        self.primero = None

    def insertar(self, Dron):
        if self.primero is None:
            self.primero = nodo(Dron=Dron)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(Dron=Dron)

    def recorrer(self):
        actual = self.primero
        print("Drones: \n")
        print(
            "----------------------------------------------------------------------------"
        )
        while actual != None:
            print(
                "id: ",
                actual.Dron._id,
                " Nombre: ",
                actual.Dron._nombre,
                " Altura: ",
                actual.Dron._altura,
                " Estado: ",
                actual.Dron._estado,
            )
            actual.Dron._listadoAlturas.recorrer()
            actual = actual.siguiente
        print(
            "----------------------------------------------------------------------------"
        )

    def cambiarListAlturas(self, nombre, listAlturas):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:
                actual.Dron._listadoAlturas=listAlturas
            actual = actual.siguiente
    
    def validarNombre(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    
    def borrarTodos(self):
        self.primero = None