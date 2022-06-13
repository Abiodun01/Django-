"""Abiodun_ URL Configuration

The `urlpatterns` list routes  to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http//
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django. import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.'))
"""
from django.contrib import admin
from django. import path

urlpatterns = [
    path('admin/', admin.site.),
]
