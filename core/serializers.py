from rest_framework import serializers

from .models import Product, Client, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_price')

    def get_price(self, obj):
        return obj.total_price()

    class Meta:
        model = Order
        fields = ('code', 'client', 'products', 'date', 'price')
