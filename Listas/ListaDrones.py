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
        result = ""
        print("Drones: \n")
        print(
            "----------------------------------------------------------------------------"
        )
        self.ordenarDrones()
        while actual != None:
            ##concatener con el resultado
            result = result + "Nombre: "+actual.Dron._nombre+"\n"
            print(
                " Nombre: ",
                actual.Dron._nombre,
                " Altura: ",
                actual.Dron._altura,
                " Estado: ",
                actual.Dron._estado,
            )
            if actual.Dron._listadoAlturas != None:
                actual.Dron._listadoAlturas.recorrer()
            actual = actual.siguiente
        print(
            "----------------------------------------------------------------------------"
        )
        return result
    
    
    

## Cambiar el listado de alturas de un dron
    def cambiarListAlturas(self, nombre, listAlturas):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:
                actual.Dron._listadoAlturas=listAlturas
            actual = actual.siguiente
    
    def instruccion(self, nombre, altura):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:                
                return actual.Dron._listadoAlturas.obtenerLetraAltura(altura)
            actual = actual.siguiente
        return "No se encontro el dron"


    def validarNombre(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    

    #ordenar drones alfabeticamente
    def ordenarDrones(self):
        actual = self.primero
        while actual != None:
            actual2 = self.primero
            while actual2 != None:
                if actual.Dron._nombre < actual2.Dron._nombre:
                    aux = actual.Dron
                    actual.Dron = actual2.Dron
                    actual2.Dron = aux
                actual2 = actual2.siguiente
            actual = actual.siguiente

            
    #obtenerAlturaInicial Dron
    def obtenerAlturaInicial(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:
                return actual.Dron._altura
            actual = actual.siguiente
        return "No se encontro el dron"
    
    def obtenerCantidadDrones(self):
        cantidad = 0
        actual = self.primero
        while actual != None:
            cantidad += 1
            actual = actual.siguiente
        return cantidad

    ##funcion para obtener dron por indice
    def obtenerDronPorIndice(self, indice):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice:
                return actual.Dron._nombre
            contador += 1
            actual = actual.siguiente
        return "nop222"
    ##actualizar Altura
    def actualizarAltura(self, nombre, altura):
        actual = self.primero
        while actual != None:
            if actual.Dron._nombre == nombre:
                actual.Dron._altura=altura
            actual = actual.siguiente

    def borrarTodos(self):
        self.primero = None