from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginRequest, name='login'),   
]