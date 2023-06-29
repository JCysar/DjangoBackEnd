from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastroUser, name='cadastro')   
]