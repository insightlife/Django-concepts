from django.contrib import admin

from django.urls import path

from formnew import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('auth',views.sup)
]
