"""inheritance URL Configuration

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
import imp
from django.contrib import admin
from django.urls import path
from demo import views
from demo.views import demon,holy,chit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('k',demon.as_view()),
    path('ok',holy.as_view()),
    path('new',chit.as_view(template='shit.html')),
    path("ch",views.chitt,{'templatename':'key.html'})
]
