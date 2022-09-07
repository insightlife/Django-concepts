from django.contrib import admin

from django.urls import path

from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set',views.set),
    path('get',views.get),
    path('function',views.function)
]
