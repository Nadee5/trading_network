from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import NetworkNode
from network.permissions import IsActiveEmployee
from network.serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """API endpoint для работы со звеньями сети.
    Поддерживаемые фильтры: country: - фильтрация звеньев сети по стране."""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [IsActiveEmployee]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
