from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),

    path('api/datos/', views.datos_sistema, name="datos"),

]