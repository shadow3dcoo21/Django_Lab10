from rest_framework import serializers
from .models import productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=productos
        fields=('codigo','descripcion','precio')