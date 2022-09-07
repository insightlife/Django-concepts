from django.urls import path

from modern_app import views

urlpatterns=[
    path('app',views.index)
]