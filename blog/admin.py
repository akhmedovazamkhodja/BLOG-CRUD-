from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_active', 'date']
    list_filter = ['date']
    search_fields = ['__all__']
    ordering = ['-date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_added']
    list_filter = ['date_added']
    search_fields = ['__all__']
    ordering = ['-date_added']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
