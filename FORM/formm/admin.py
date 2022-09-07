from django.contrib import admin

from formm.models import  student_no

class student_info(admin.ModelAdmin):
    list_display = ['id','email']

admin.site.register(student_no,student_info)
