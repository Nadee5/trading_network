from django.utils.html import format_html
from django.utils.safestring import mark_safe
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from network.models import NetworkNode
from products.serializers import ProductSerializer


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели NetworkNode."""

    products_count = serializers.SerializerMethodField()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ['products_count']

    def get_fields(self):
        fields = super().get_fields()
        request_method = self.context['request'].method

        if request_method == 'POST':
            del fields['level']
        elif request_method == 'PUT' or request_method == 'PATCH':
            del fields['debt']
            del fields['level']

        return fields

    def get_products_count(self, instance):
        return instance.products.count()
