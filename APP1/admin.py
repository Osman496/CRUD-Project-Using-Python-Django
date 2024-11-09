# This code snippet is from a Django project. Here's what it does:
from django.contrib import admin
from .models import Stu_Data
# Register your models here.


@admin.register(Stu_Data)
class Stu_DataAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'email', 'password','address')
