from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from suppliers.models import NetworkNode
from suppliers.permissions import IsActiveStaff
from suppliers.serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    CRUD контроллер для работы с торговой сетью
    CRUD операции:
    1) Получить список объектов: GET /nodes/
    2) Создать новый объект: POST /nodes/
    3) Получить информацию об объекте: GET /nodes/{id}/
    4) Обновить объект: PUT /nodes/{id}/ (поле debt обновлено не будет)
    5) Удалить объект: DELETE /nodes/{id}/
    6) Фильтрация по стране GET /nodes/?country=Russia
    """

    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaff]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ["country"]
    search_fields = ["name", "city"]
