"""
Здесь описаны сериализаторы для моделей поставщиков
"""
from rest_framework import serializers
from suppliers.models import Contacts, Products, Factory, RetailNetwork, IndividualEntrepreneur
from django.contrib.contenttypes.models import ContentType


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для контакта"""
    class Meta:
        model = Contacts
        fields: list[str] = ['email', 'country', 'city', 'city', 'house']


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для товара"""
    class Meta:
        model = Products
        fields: list[str] = ['name', 'model', 'data']


class FactorySerializer(serializers.ModelSerializer):
    """Сериализатор для завода"""
    contacts: ContactSerializer = ContactSerializer()
    products: ProductSerializer = ProductSerializer()

    class Meta:
        model = Factory
        fields: list[str] = ['name', 'contacts', 'products', 'date']


class RetailNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для розничной сети"""
    contacts: ContactSerializer = ContactSerializer()
    products: ProductSerializer = ProductSerializer()
    supplier: FactorySerializer = FactorySerializer()

    class Meta:
        model = RetailNetwork
        fields: list[str] = ['name', 'contacts', 'products', 'supplier', 'arrears', 'date']


class GenericRelatedField(serializers.RelatedField):
    """Данный класс используется для сериализации связанных объектов"""
    def to_representation(self, value):
        if isinstance(value, Factory):
            serializer = FactorySerializer(value)
        elif isinstance(value, RetailNetwork):
            serializer = RetailNetworkSerializer(value)
        else:
            raise ValueError(f'Unknown object type: {type(value)}')
        return serializer.data

    def to_internal_value(self, data):
        try:
            model = ContentType.objects.get(model=data['supplier_content_type']).model_class()
            return model.objects.get(pk=data['supplier_object_id'])
        except (KeyError, ContentType.DoesNotExist):
            raise serializers.ValidationError('Supplier does not exist')


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    """Сериализатор для индивидуального предпринимателя"""
    contacts: ContactSerializer = ContactSerializer()
    products: ProductSerializer = ProductSerializer()
    supplier: GenericRelatedField = GenericRelatedField(read_only=True)

    class Meta:
        model = IndividualEntrepreneur
        fields: list[str] = ['name', 'contacts', 'products', 'supplier', 'arrears', 'date']

    def create(self, validated_data):
        """Создание индивидуального предпринимателя"""
        supplier_data = validated_data.pop('supplier')
        individual_entrepreneur = IndividualEntrepreneur.objects.create(
            supplier_content_type = ContentType.objects.get_for_model(supplier_data),
            supplier_object_id = supplier_data.pk,
            **validated_data
        )
        return individual_entrepreneur
