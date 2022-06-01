from rest_framework import serializers
from .models import *

class WarehouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
        