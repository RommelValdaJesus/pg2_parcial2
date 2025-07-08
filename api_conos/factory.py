class ConoBase:
    def __init__(self):
        self.ingredientes = []
        self.precio = 0.0

    def inicializar(self):
        raise NotImplementedError

class Carnivoro(ConoBase):
    def inicializar(self):
        self.ingredientes = ["pollo", "salchicha"]
        self.precio = 15.0

class Vegetariano(ConoBase):
    def inicializar(self):
        self.ingredientes = ["verduras salteadas", "queso"]
        self.precio = 12.0

class Saludable(ConoBase):
    def inicializar(self):
        self.ingredientes = ["espinaca", "aguacate"]
        self.precio = 13.0

class ConoFactory:
    @staticmethod
    def obtener_cono(variante):
        mapeo = {
            "Carnívoro": Carnivoro,
            "Vegetariano": Vegetariano,
            "Saludable": Saludable
        }
        if variante not in mapeo:
            raise ValueError("Variante no válida")
        cono = mapeo[variante]()
        cono.inicializar()
        return cono