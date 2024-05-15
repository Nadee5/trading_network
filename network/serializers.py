from rest_framework import serializers

from network.models import NetworkNode
from products.serializers import ProductSerializer


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели NetworkNode."""

    products_count = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ['level']

    def get_fields(self):
        """Получает список полей для сериализатора в зависимости от HTTP-метода запроса.
        Поле debt закрыто для изменений."""
        fields = super().get_fields()
        request_method = self.context['request'].method

        if request_method == 'PUT' or request_method == 'PATCH':
            del fields['debt']

        return fields

    def get_products_count(self, instance):
        """Считает количество продуктов компании."""
        return instance.products.count()
