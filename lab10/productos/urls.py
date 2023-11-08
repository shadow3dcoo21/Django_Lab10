from django.urls import path,include
from rest_framework import routers

from . import views


router=routers.DefaultRouter()
router.register('productos',views.ProductosViewSet)

urlpatterns=[
    path('',include(router.urls))
]