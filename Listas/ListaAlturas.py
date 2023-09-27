from Altura import Altura


class nodo:
    def __init__(self, Altura=None, siguiente=None):
        self.Altura = Altura
        self.siguiente = siguiente


class lista_Alturas:
    def __init__(self):
        self.primero = None

    def insertar(self, Altura):
        if self.primero is None:
            self.primero = nodo(Altura=Altura)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(Altura=Altura)

    def recorrer(self):
        actual = self.primero
        print("-- Alturas Dron--- \n")
        print(
            "----------------------------------------------------------------------------"
        )
        while actual != None:
            print(
                "Altura: ",
                actual.Altura._altura,
                " Letra: ",
                actual.Altura._letra,
            )
            actual = actual.siguiente
        print(
            "----------------------------------------------------------------------------"
        )

    def obtenerLetraAltura(self, altura):
        actual = self.primero
        while actual != None:
            if actual.Altura._altura == altura:
                return actual.Altura._letra
            actual = actual.siguiente
        return None
    
    def borrarTodos(self):
        self.primero = None