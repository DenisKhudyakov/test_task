"""
Здесь описаны сериализаторы для моделей поставщиков
"""

from rest_framework import serializers

from suppliers.models import NetworkNode, Products


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для товара"""

    class Meta:
        model = Products
        fields: list[str] = ["id", "name", "model", "data"]


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для торгующей сети"""

    products: ProductSerializer = ProductSerializer(many=True, read_only=True)
    hierarchy_level = serializers.IntegerField(
        source="get_hierarchy_level", read_only=True
    )

    class Meta:
        model = NetworkNode
        fields: list[str] = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "debt",
            "creation_date",
            "hierarchy_level",
            "products",
        ]
        read_only_fields: list[str] = ["debt"]
