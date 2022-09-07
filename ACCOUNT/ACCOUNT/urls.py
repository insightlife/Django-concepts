from django.contrib import admin

from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.user_signup),
    path('login',views.user_login),
    path('profile',views.user_profile),
    path('logout',views.user_logout),
    path('changepass',views.changepass)
]
