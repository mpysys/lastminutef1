from django.contrib import admin
from .models import TicketOrder, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class TicketOrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('ticket_number', 'date',
                       'discount_value', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('ticket_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'discount_value',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('ticket_number', 'date', 'full_name',
                    'order_total', 'discount_value',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(TicketOrder, TicketOrderAdmin)
