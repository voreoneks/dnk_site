from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('user_visible', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title', )}

