"""
Здесь находятся модели приложения поставщиков и их связи
Модели: Завод, Индивидуальный Предприниматель, Розничная Сеть, Контакты, Продукты
"""

import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from config.settings import NULLABLE


class Contacts(models.Model):
    """Модель контактов поставщика"""

    email: str = models.EmailField(max_length=100, unique=True, verbose_name="Email")
    country: str = models.CharField(max_length=50, verbose_name="Страна")
    city: str = models.CharField(max_length=50, verbose_name="Город")
    street: str = models.CharField(max_length=50, verbose_name="Улица")
    house: str = models.CharField(max_length=10, verbose_name="Дом")

    def __str__(self) -> str:
        return f"{self.email}, {self.country}, {self.city}, {self.street}, {self.house}"

    class Meta:
        verbose_name: str = "Контакт"
        verbose_name_plural: str = "Контакты"


class Products(models.Model):
    """Модель продуктов поставщика"""

    name: str = models.CharField(max_length=50, verbose_name="Название")
    model: str = models.CharField(max_length=50, verbose_name="Модель")
    data: str = models.DateField(verbose_name="Дата выпуска")

    def __str__(self) -> str:
        return f"{self.name}, {self.model}, {self.data}"

    class Meta:
        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"


class Factory(models.Model):
    """
    Модель завода, это производитель, он имеет нулевой уровень иерархии среди всех поставщиков
    по ТЗ должно быть поле задолженности, но т.к. завод имеет нулевой уровень в иерархии,
    по умолчанию он никому не должен
    """

    name: str = models.CharField(max_length=50, verbose_name="Название")
    contacts: Contacts = models.OneToOneField(
        Contacts, on_delete=models.CASCADE, verbose_name="Контакты", **NULLABLE
    )
    products: Products = models.ManyToManyField(
        Products, verbose_name="Продукты", **NULLABLE
    )
    date: str = models.DateField(
        verbose_name="Дата создания организации", default=datetime.date.today
    )

    def __str__(self) -> str:
        return f"{self.name}, {self.contacts}, {self.products}"

    class Meta:
        verbose_name: str = "Завод"
        verbose_name_plural: str = "Заводы"


class RetailNetwork(models.Model):
    """
    Модель розничной сети, уровень в иерархии №1, официальный диллер завода изготовителя
    Может иметь задолженность перед заводом
    """

    name: str = models.CharField(max_length=50, verbose_name="Название")
    contacts: Contacts = models.OneToOneField(
        Contacts, on_delete=models.CASCADE, verbose_name="Контакты", **NULLABLE
    )
    products: Products = models.ManyToManyField(
        Products, verbose_name="Продукты", **NULLABLE
    )
    supplier: Factory = models.ForeignKey(
        Factory, on_delete=models.CASCADE, verbose_name="Поставщик", **NULLABLE
    )
    arrears: float = models.FloatField(verbose_name="Сумма задолженности", default=0)
    date: str = models.DateField(
        verbose_name="Дата создания организации", default=datetime.date.today
    )

    def __str__(self) -> str:
        return f"{self.name}, {self.contacts}, {self.products}, {self.arrears}"

    class Meta:
        verbose_name: str = "Розничная сеть"
        verbose_name_plural: str = "Розничные сети"


class IndividualEntrepreneur(models.Model):
    """
    Класс индивидуального предпринимателя, уровень в иерархии может быть любым, кроме 0,
    может иметь задолженность перед заводом и перед розничной сетью,
    поставщики: Завод, Розничная сеть
    """

    name: str = models.CharField(max_length=50, verbose_name="Название")
    contacts: Contacts = models.OneToOneField(
        Contacts, on_delete=models.CASCADE, verbose_name="Контакты", **NULLABLE
    )
    products: Products = models.ManyToManyField(
        Products, verbose_name="Продукты", **NULLABLE
    )
    supplier_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Тип поставщика",
        limit_choices_to={"model__in": ("Factory", "RetailNetwork")},
        **NULLABLE,
    )
    supplier_object_id = models.PositiveIntegerField(
        verbose_name="ID поставщика", **NULLABLE
    )
    supplier = GenericForeignKey("supplier_content_type", "supplier_object_id")
    arrears: float = models.FloatField(verbose_name="Сумма задолженности", default=0)
    date: str = models.DateField(
        verbose_name="Дата создания организации", default=datetime.date.today
    )

    def __str__(self) -> str:
        return f"{self.name}, {self.contacts}, {self.products}, {self.supplier}"

    class Meta:
        verbose_name: str = "Индивидуальный предприниматель"
        verbose_name_plural: str = "Индивидуальные предприниматели"
