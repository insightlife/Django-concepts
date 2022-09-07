from django.contrib import admin

from django.urls import path

from formm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('form',views.student_info),
    path('kit',views.kit)
]
