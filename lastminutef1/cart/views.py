from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from tickets.models import Ticket

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified ticket to the shopping cart """

    ticket = get_object_or_404(Ticket, pk=item_id) 
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    racelength = None
    if 'race_length' in request.POST:
        racelength = request.POST['race_length']
    cart = request.session.get('cart', {})

    if racelength:
        if item_id in list(cart.keys()):
            if racelength in cart[item_id]['race_by_length'].keys():
                cart[item_id]['race_by_length'][racelength] += quantity
                messages.success(request, f'Updated racelength {racelength.upper()} {ticket.race} quantity to {cart[item_id]["race_by_length"][racelength]}')
            else:
                cart[item_id]['race_by_length'][racelength] = quantity
                messages.success(request, f'Added racelength {racelength.upper()} {ticket.race} to your cart')
        else:
            cart[item_id] = {'race_by_length': {racelength: quantity}}
            messages.success(request, f'Added racelength {racelength.upper()} {ticket.race} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {ticket.race} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {ticket.race} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
