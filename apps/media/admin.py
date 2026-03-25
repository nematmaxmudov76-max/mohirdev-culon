from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_url', 'created_at')
    search_fields = ('file_url',)
    list_filter = ('created_at',)

