from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    ticket_count = 0

    if total < settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_PROMOTION_PERCENTAGE  / 100)
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        discount = 0
        discount_delta = 0

    grand_total = discount + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'ticket_count': ticket_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
