from django.contrib import admin

from workers.models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """Админ панель работника"""

    list_display = (
        "id",
        "name",
        "email",
        "company",
    )
