from django.urls import path
from . import views


urlpatterns = [
    path('estoque/', views.estoqueView, name='estoque'),
    
]