"""
Здесь находятся модели приложения поставщиков
Модель NetworkNode может быть одной из следующих: Завод, Индивидуальный Предприниматель, Розничная Сеть
Модель Product это продукт, которые реализует поставщик
"""

from django.utils import timezone

from django.db import models

from config.settings import NULLABLE


class NetworkNode(models.Model):
    """Модель для хранения данных сетевого узла"""

    name: str = models.CharField(max_length=50, verbose_name="Название")

    email: str = models.EmailField(max_length=100, unique=True, verbose_name="Email")
    country: str = models.CharField(max_length=50, verbose_name="Страна")
    city: str = models.CharField(max_length=50, verbose_name="Город")
    street: str = models.CharField(max_length=50, verbose_name="Улица")
    house_number: str = models.CharField(max_length=10, verbose_name="Дом")

    supplier: int = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE)
    debt: float = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Дебеторская задолженность"
    )
    creation_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )

    def get_hierarchy_level(self) -> int:
        level = 0
        current_node = self.supplier
        while current_node:
            level += 1
            current_node = current_node.supplier
        return level

    def __str__(self) -> str:
        return f"{self.name}, {self.email}, {self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name: str = "Сетевой узел"
        verbose_name_plural: str = "Сетевые узлы"


class Products(models.Model):
    """Модель продуктов поставщика"""

    name: str = models.CharField(max_length=50, verbose_name="Название")
    model: str = models.CharField(max_length=50, verbose_name="Модель")
    data: str = models.DateField(verbose_name="Дата выпуска")

    network_node: NetworkNode = models.ForeignKey(
        NetworkNode, on_delete=models.CASCADE, **NULLABLE, verbose_name="Торгующая сеть"
    )

    def __str__(self) -> str:
        return f"{self.name}, {self.model}, {self.data}"

    class Meta:
        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"
