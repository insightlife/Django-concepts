from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('response',views.response),
    path('hello',views.thanks)
]