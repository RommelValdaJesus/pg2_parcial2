from api_conos.models import PedidoCono

class ConoPersonalizadoBuilder:
    def __init__(self, base_cono):
        self.base = base_cono
        self.precio = base_cono.precio
        self.ingredientes = list(base_cono.ingredientes)

    def agregar_toppings(self, toppings):
        for t in toppings:
            if t not in PedidoCono.TOPPINGS_VALIDOS:
                raise ValueError(f"Topping '{t}' inválido.")
            self.ingredientes.append(t)
            self.precio += PedidoCono.TOPPINGS_VALIDOS[t]

    def ajustar_tamanio(self, tamaño):
        if tamaño == "Mediano":
            self.precio *= 1.2
        elif tamaño == "Grande":
            self.precio *= 1.5

    def obtener_precio(self):
        return round(self.precio, 2)

    def obtener_ingredientes(self):
        return self.ingredientes