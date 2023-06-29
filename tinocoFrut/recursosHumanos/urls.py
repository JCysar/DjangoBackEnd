from django.urls import path
from . import views


urlpatterns = [
    path('recursosHumanos/', views.recursosHumanosCadastroView, name='recursosHumanos'),   
]