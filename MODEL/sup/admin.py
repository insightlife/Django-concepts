from django.contrib import admin

from sup.models import info

class infoo(admin.ModelAdmin):
    list_display = ['name','age']

admin.site.register(info,infoo)
