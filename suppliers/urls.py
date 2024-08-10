"""
CRUD операции:
1) Получить список объектов: GET /nodes/
2) Создать новый объект: POST /nodes/
3) Получить информацию об объекте: GET /nodes/{id}/
4) Обновить объект: PUT /nodes/{id}/ (поле debt обновлено не будет)
5) Удалить объект: DELETE /nodes/{id}/
6) Фильтрация по стране GET /nodes/?country=Russia
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from suppliers.apps import SuppliersConfig
from suppliers.views import NetworkNodeViewSet

app_name = SuppliersConfig.name

router = DefaultRouter()
router.register("nodes", NetworkNodeViewSet, basename="nodes")
urlpatterns = [
    path("", include(router.urls)),
]
