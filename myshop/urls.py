"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from account import views as account_views
from shop import views as shop_views
from django.conf.urls.static import static
from django.conf.urls import url



'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('shop.urls', namespace='shop')),
]

urlpatterns = [
    path('', include('shop.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken'))
]'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/', include('shop.urls')),
	path('api1/v1/register/', account_views.RegisterAPIView.as_view()),
    path('api1/v1/login/', account_views.LoginAPIView.as_view()),
    path('api1/v1/confirm/', account_views.ConfirmAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)