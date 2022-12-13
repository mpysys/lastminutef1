from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import TicketOrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('tickets'))

    ticket_order_form = TicketOrderForm()
    template = 'checkout.html'
    context = {
        'ticket_order_form': ticket_order_form,
        'stripe_public_key': 'pk_test_51MBnrnDhtt0ii4VPb4IM65cqw91CBqmzS4ZiVYxjQ7RK5hWysKflAV42kCz9OITXjK9RK9OHny8pay1RsDIrY5x50031bPwNY1',
        'client_secret' : 'test client secret',
    }

    return render(request, template, context)