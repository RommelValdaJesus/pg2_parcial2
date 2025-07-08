from django.db import models

class PedidoCono(models.Model):
    VARIANTES = [
        ("Carnívoro", "Carnívoro"),
        ("Vegetariano", "Vegetariano"),
        ("Saludable", "Saludable"),
    ]
    TAMAÑOS = [
        ("Pequeño", "Pequeño"),
        ("Mediano", "Mediano"),
        ("Grande", "Grande"),
    ]
    cliente = models.CharField(max_length=100)
    variante = models.CharField(max_length=20, choices=VARIANTES)
    toppings = models.JSONField(default=list, blank=True)
    tamanio_cono = models.CharField(max_length=10, choices=TAMAÑOS)
    fecha_pedido = models.DateField(auto_now_add=True)

    TOPPINGS_VALIDOS = {
        "queso_extra": 1.0,
        "papas_al_hilo": 0.5,
        "salchicha_extra": 1.5,
        "guacamole": 2.0,
        "soya_texturizada": 1.2,
        "sal": 0.1,
    }

    def clean(self):
        toppings_invalidos = [t for t in self.toppings if t not in self.TOPPINGS_VALIDOS]
        if toppings_invalidos:
            from django.core.exceptions import ValidationError
            raise ValidationError(f"Toppings inválidos: {', '.join(toppings_invalidos)}")