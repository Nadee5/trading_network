from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from network.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    exclude = ('level',)
    list_display = ('pk', 'name', 'city', 'level', 'supplier', 'supplier_link', 'debt',)
    list_filter = ('city', 'level',)
    actions = ['clear_debt_to_supplier']

    search_fields = ('name', 'country', 'supplier',)
    ordering = ('pk', 'name', 'debt',)

    def supplier_link(self, obj):
        """Метод для отображения ссылки на страницу изменения объекта поставщика."""
        if obj.supplier:
            url = reverse('admin:network_networknode_change', args=[obj.supplier.id])
            link = '<a href="{}">Поставщик</a>'.format(url)
            return mark_safe(link)
        return 'Нет поставщика'
    supplier_link.short_description = 'Карточка поставщика'

    def clear_debt_to_supplier(self, request, queryset):
        """Метод custom admin action - Сброс задолженности перед поставщиком."""
        queryset.update(debt=0)
    clear_debt_to_supplier.short_description = 'Очистить задолженность перед поставщиком'
