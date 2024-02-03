from django.urls import  path
from .views import *

urlpatterns = [
        path('', index, name='index'),
        path('code39/', code39, name='code39'),
        path('code128/', code128, name='code128'),
        path('ean8/', ean8, name='ean8'),
        path('ean13/', ean13, name='ean13'),
        path('ean14/', ean14, name='ean14'),
        # path('prueba/', prueba, name='prueba'),

]
