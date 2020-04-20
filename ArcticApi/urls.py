"""ArcticApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from api import views


urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('appstore/<int:pk>/', views.AppStoreDetail.as_view()),
    path('appstore/',views.AppStoreList.as_view()), #for is415
    path('admin/', admin.site.urls),
    path('azure/', views.AzureML.as_view()), #azure api call

    path('api/', include('api.urls')),
    path('sale/',views.CreatSale.as_view())

]