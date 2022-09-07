from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic_app/',include('basic_app.url')),
    path('modern_app/',include('modern_app.url'))
]
