from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tickets.models import Ticket


def cart_contents(request):

    cart_items = []
    total = 0
    ticket_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            ticket = get_object_or_404(Ticket, pk=item_id)
            total += item_data * ticket.price
            ticket_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'ticket': ticket,
            })
        else:
            ticket = get_object_or_404(Ticket, pk=item_id)
            for racelength, quantity in item_data['race_by_length'].items():
                total += quantity * ticket.price
                ticket_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'ticket': ticket,
                    'racelength': racelength,
                })

    if total > settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    
    grand_total = total - discount 
    
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
