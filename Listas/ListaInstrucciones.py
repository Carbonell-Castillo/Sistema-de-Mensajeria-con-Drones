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
    
    ##validar si en un timpo t el estado esta "Emitir luz"
    def validarEstado(self, tiempo):
        actual = self.primero
        while actual != None:
            if actual.Instruccion._tiempo == tiempo and actual.Instruccion._estado == "Emitir Luz":
                print("El dron: ", actual.Instruccion._nombreDron, " emitio luz en el tiempo: ", tiempo)
                return True
            actual = actual.siguiente
        return False
    
    ##Funcion para obtener el tiempo mayor de todos los registros
    def obtenerTiempoMayor(self):
        tiempo_mayor = 0
        actual = self.primero
        while actual != None:
            if actual.Instruccion._tiempo > tiempo_mayor:
                tiempo_mayor = actual.Instruccion._tiempo
            actual = actual.siguiente
        return tiempo_mayor
    
    ##funcion que regresa lista de instrucciones que tengan solo esa altura
    def obtenerInstruccionesTiempo(self, tiempo):
        lista = lista_Instrucciones()
        actual = self.primero
        while actual != None:
            if actual.Instruccion._tiempo == tiempo:
                lista.insertar(actual.Instruccion)
            actual = actual.siguiente
        return lista

    #obtener instrucciones por altura y nombre
    def obtenerInstruccionesAlturaNombre(self, tiempo, nombre):
        actual = self.primero
        while actual != None:
            if actual.Instruccion._tiempo == tiempo and actual.Instruccion._nombreDron == nombre:
                return actual.Instruccion
            actual = actual.siguiente
        return None
    

    def obtenerUltimoDron(self, nombre):
        ultimo_dron = None
        actual = self.primero
        while actual != None:
            if actual.Instruccion._nombreDron == nombre:
                ultimo_dron = actual.Instruccion._tiempo
            actual = actual.siguiente
        return ultimo_dron

    #obtenerCantidadInstrucciones
    def obtenerCantidadInstrucciones(self):
        cantidad = 0
        actual = self.primero
        while actual != None:
            cantidad += 1
            actual = actual.siguiente
        return cantidad

    #obtener instruccion indice y que el _tiempo sea igual
    def obtenerInstruccionIndice(self, indice, tiempo):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice and actual.Instruccion._tiempo == tiempo:
                return actual.Instruccion
            contador += 1
            actual = actual.siguiente
        return None

    #obtener instrucciones indiceSolo
    def obtenerInstruccionIndiceSolo(self, indice):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice:
                return actual.Instruccion
            contador += 1
            actual = actual.siguiente
        return None
    
    def borrarTodos(self):
        self.primero = None