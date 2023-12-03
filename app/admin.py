from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency')


admin.site.register(Item, ItemAdmin)
