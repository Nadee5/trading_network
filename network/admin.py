from django.contrib import admin

from network.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    exclude = ('level',)
    list_display = ('pk', 'name', 'email', 'country', 'supplier', 'level', 'debt',)
    list_filter = ('country', 'city',)
    search_fields = ('name', 'country', 'supplier',)
    ordering = ('pk', 'name', 'debt',)
