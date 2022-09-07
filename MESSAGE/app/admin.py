from django.contrib import admin

# Register your models here.
from .models import user
@admin.register(user)
class adminuser(admin.ModelAdmin):
    list_display=('id','name','password')

