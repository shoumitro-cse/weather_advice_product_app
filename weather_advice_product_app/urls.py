"""weather_advice_product_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from accounts.serializer import TokenObtainPairSerializer

urlpatterns = [
    # for default admin panel
    path('admin/', admin.site.urls),

    # add accounts urls
    path('api/accounts/', include('accounts.urls')),

    # add weather urls
    path('api/', include('weather.urls')),

    # add ProductT urls
    path('api/', include('products.urls')),

    # Token authentication for API
    path('api/token/', TokenObtainPairView.as_view(serializer_class=TokenObtainPairSerializer),
         name='token_obtain_pair_api'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_api'),

    # for API docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redocs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
