class Conobase:

    def __init__(self):
        self.ingredientes = []
        self.precio = 0

    def inicializar(self):
        """Define los ingredientes y el precio base. Implementado por subclases."""
        raise NotImplementedError()

    def obtener_ingredientes_base(self):
        return self.ingredientes

    def precio_base(self):
        return self.precio
    

class ConoCarnivoro(Conobase):
    def iniciarlizar(self):
        self.ingredientes = ['pollo', 'carne', 'tocino']
        self.precio = 5.0

class ConoVegetariano(Conobase):
    def iniciarlizar(self):
        self.ingredientes = ['tomate', 'lechuga', 'pimiento']
        self.precio = 4.0

class ConoSaludable(Conobase):
    def iniciarlizar(self):
        self.ingredientes = ['zanahoria', 'brocoli', 'pepino']
        self.precio = 3.5