"""mainproject URL Configuration

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
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('display',views.display,name='display'),
    path('forContrib',views.forContrib,name='Contrib'),
    path('fortheProject',views.fortheProject,name='theProject'),
    path('convert',views.convert,name='convert'),
    path('convertPng',views.convert,name='convert'),
    path('imgTopdf',views.imgTopdf,name='imgTopdf'),
    path('pngToJpg',views.pngToJpg,name='pngToJpg'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 