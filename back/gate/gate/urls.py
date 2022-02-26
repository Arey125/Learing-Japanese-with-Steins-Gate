"""gate URL Configuration

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
from django.urls import path, re_path
from application import views

urlpatterns = [
    path('', views.index),
    re_path(r'^upload', views.upload_db),
    re_path(r'^file', views.get_file),
    re_path(r'^sentence', views.get_sentence),
    re_path(r'^voice/(?P<name>.+)/', views.get_voice),
    re_path(r'^merge', views.merge),
    re_path(r'^split', views.split),
    re_path(r'^mark', views.mark),
    re_path(r'^export', views.export),
]
