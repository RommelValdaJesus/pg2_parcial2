# views.py
from rest_framework import viewsets
from api_conos.models import PedidoCono
from api_conos.serializers import PedidoConoSerializer

class PedidoConoViewSet(viewsets.ModelViewSet):
    queryset = PedidoCono.objects.all().order_by("-fecha_pedido")
    serializer_class = PedidoConoSerializer