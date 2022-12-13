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
    }

    return render(request, template, context)