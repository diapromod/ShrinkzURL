from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at')  # Adjust fields as per your model
    search_fields = ('original_url', 'short_code')
