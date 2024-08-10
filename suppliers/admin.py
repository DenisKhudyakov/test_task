from django.contrib import admin

from suppliers.models import NetworkNode, Products


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """Админ панель сети"""
    list_display: tuple[str] = (
        "id",
        "name",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "supplier",
        "debt",
        "creation_time",
        "hierarchy_level",
        "products",
    )
    list_filter: tuple[str] = ("city",)
    search_fields: tuple[str] = ("name", "city",)
    actions = ["clear_debt",]

    def supplier_link(self, obj):
        """Ссылка на товар"""
        if obj.supplier:
            return f'<a href="/admin/suppliers/networknode/{obj.supplier.id}/change/">{obj.supplier.name}</a>'
        return "Нет данных поставщика"

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        """Очистка долга"""
        queryset.update(debt=0.00)
        self.message_user(request, "Долг очищен")

    clear_debt.short_description = "Очистить долг"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """Админ панель товаров"""
    list_display: tuple[str] = ("id", "name", "model", "data")
    search_fields: tuple[str] = ("name", "model",)