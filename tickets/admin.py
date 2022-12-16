from django.contrib import admin
from .models import Ticket, Category
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'race',
        'country',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Category, CategoryAdmin)
