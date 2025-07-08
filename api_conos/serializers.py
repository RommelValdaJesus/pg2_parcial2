# serializers.py
from rest_framework import serializers
from api_conos.models import PedidoCono
from api_conos.factory import ConoFactory
from api_conos.builder import ConoPersonalizadoBuilder
from api_patrones.logger import LoggerSingleton
from rest_framework.exceptions import ValidationError

class PedidoConoSerializer(serializers.ModelSerializer):
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = "__all__"

    def _build_cono(self, obj):
        base = ConoFactory.obtener_cono(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        builder.agregar_toppings(obj.toppings)
        builder.ajustar_tamanio(obj.tamanio_cono)
        return builder

    def get_precio_final(self, obj):
        logger = LoggerSingleton()
        builder = self._build_cono(obj)
        precio = builder.obtener_precio()
        logger.registrar(f"Calculado precio para pedido {obj.id}: {precio}")
        return precio

    def get_ingredientes_finales(self, obj):
        logger = LoggerSingleton()
        builder = self._build_cono(obj)
        ingredientes = builder.obtener_ingredientes()
        logger.registrar(f"Ingredientes finales para pedido {obj.id}: {ingredientes}")
        return 
    
   