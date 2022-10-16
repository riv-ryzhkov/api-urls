from django.contrib import admin
from .models import Urls

# Register models here for admin.


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'host_url', 'short_url', 'created')
    list_display_links = ('id', 'host_url')
    search_fields = ('id', 'host_url', 'short_url', 'created')
    list_editable = ('short_url',)
    list_filter = ('host_url', 'short_url', 'created')


admin.site.register(Urls, UrlsAdmin)