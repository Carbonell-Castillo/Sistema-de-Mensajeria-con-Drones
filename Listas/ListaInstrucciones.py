from Instruccion import Instruccion


class nodo:
    def __init__(self, Instruccion=None, siguiente=None):
        self.Instruccion = Instruccion
        self.siguiente = siguiente


class lista_Instrucciones:
    def __init__(self):
        self.primero = None

    def insertar(self, Instruccion):
        if self.primero is None:
            self.primero = nodo(Instruccion=Instruccion)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(Instruccion=Instruccion)

    def recorrer(self):
        actual = self.primero
        print("Instrucciones: \n")
        print(
            "----------------------------------------------------------------------------"
        )
        while actual != None:
            print(
                "T: ",
                actual.Instruccion._tiempo,
                " Nombre Dron: ",
                actual.Instruccion._nombreDron,
                " Estado: ",
                actual.Instruccion._estado,
            )
            actual = actual.siguiente
        print(
            "----------------------------------------------------------------------------"
        )

    ##ordenar lista por orden alfabeticod de nombreDron y por tiempo
    def ordenar(self):
        actual = self.primero
        while actual != None:
            siguiente = actual.siguiente
            while siguiente != None:
                if actual.Instruccion._nombreDron > siguiente.Instruccion._nombreDron:
                    aux = actual.Instruccion
                    actual.Instruccion = siguiente.Instruccion
                    siguiente.Instruccion = aux
                elif actual.Instruccion._nombreDron == siguiente.Instruccion._nombreDron:
                    if actual.Instruccion._tiempo > siguiente.Instruccion._tiempo:
                        aux = actual.Instruccion
                        actual.Instruccion = siguiente.Instruccion
                        siguiente.Instruccion = aux
                siguiente = siguiente.siguiente
            actual = actual.siguiente
    
    
    ##Funcion para obtener el tiempo mayor de todos los registros
    def obtenerTiempoMayor(self):
        tiempo_mayor = 0
        actual = self.primero
        while actual != None:
            if actual.Instruccion._tiempo > tiempo_mayor:
                tiempo_mayor = actual.Instruccion._tiempo
            actual = actual.siguiente
        return tiempo_mayor
    

    

    def obtenerUltimoDron(self, nombre):
        ultimo_dron = None
        actual = self.primero
        while actual != None:
            if actual.Instruccion._nombreDron == nombre:
                ultimo_dron = actual.Instruccion._tiempo
            actual = actual.siguiente
        return ultimo_dron


    
    def borrarTodos(self):
        self.primero = None