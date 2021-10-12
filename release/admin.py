from django.contrib import admin
from .models import *

@admin.register(MainInfo)
class MainInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'is_update_photo', 'user')


