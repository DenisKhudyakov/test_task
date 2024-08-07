from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import NULLABLE


class Worker(AbstractUser):
    """Модель пользователя, он же рабочий компании"""
    name: str = models.CharField(max_length=100, verbose_name="Имя")
    email: str = models.EmailField(unique=True, verbose_name="Email", **NULLABLE)
    company: str = models.CharField(max_length=100, verbose_name="Компания", **NULLABLE)

    def __str__(self) -> str:
        return self.name

    REQUIRED_FIELDS: list[str,] = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"