from django.shortcuts import render
from rest_framework import viewsets

from .serializer import ProductosSerializer
from .models import productos


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = productos.objects.all()
    serializer_class = ProductosSerializer
# Create your views here.
