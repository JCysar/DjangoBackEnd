
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include('login.urls')),
    path('', include('cadastro.urls')),
    path('', include('produtos.urls')),
    path('', include('financeiro.urls')),
    path('', include('estoque.urls')),
    path('', include('recursosHumanos.urls')),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
