from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'gender', 'type', 'date_made', 'is_active']
    list_filter = ['date_of_birth', 'type']
    search_fields = ['__all__']
    ordering = ['-date_made']

admin.site.register(Profile, ProfileAdmin)