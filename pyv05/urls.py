"""pyv05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from indexs import views_index
from app_get_data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_index.index),
    path('api/v0.5/', include('pyv05.version_1_0')),
    path('title/', views.json_test),
    path('body/', views.index_scetc_news),
    # iot_api
    path('sensor/', views_index.iot_sensor),
    path('iot/', views_index.api_iot.as_view()),
]
