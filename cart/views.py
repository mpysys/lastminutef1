from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
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
                messages.success(request, f'Updated {racelength.upper()} day \
                                tickets for the {ticket.race} race \
                                to x \
                                {cart[item_id]["race_by_length"][racelength]}')
            else:
                cart[item_id]['race_by_length'][racelength] = quantity
                messages.success(request, f'Added {racelength.upper()} \
                                day tickets for the {ticket.race} \
                                race to your cart')
        else:
            cart[item_id] = {'race_by_length': {racelength: quantity}}
            messages.success(request, f'Added {racelength.upper()} day \
                            tickets for the {ticket.race} race to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {ticket.race} \
                            race tickets to x {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {ticket.race} \
                            race tickets to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified ticket to the shopping cart """

    ticket = get_object_or_404(Ticket, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    racelength = None
    if 'race_length' in request.POST:
        racelength = request.POST['race_length']
    cart = request.session.get('cart', {})

    if racelength:
        if quantity > 0:
            cart[item_id]['race_by_length'][racelength] = quantity
            messages.success(request, f'Updated {racelength.upper()} day \
                            tickets for the {ticket.race} race \
                            x {cart[item_id]["race_by_length"][racelength]}')
        else:
            del cart[item_id]['race_by_length'][racelength]
            if not cart[item_id]['race_by_length']:
                cart.pop(item_id)
            messages.success(request, f'Removed {racelength.upper()} day \
                            tickets for the {ticket.race} race from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {ticket.race} \
                            ticket quantity to x {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed tickets \
                            for {ticket.race} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item / ticket from the shopping cart """
    try:
        ticket = get_object_or_404(Ticket, pk=item_id)
        racelength = None
        if 'race_length' in request.POST:
            racelength = request.POST['race_length']
        cart = request.session.get('cart', {})

        if racelength:
            del cart[item_id]['race_by_length'][racelength]
            if not cart[item_id]['race_by_length']:
                cart.pop(item_id)
            messages.success(request, f'Removed all {racelength.upper()} \
                            ticket for the {ticket.race} race from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {ticket.race} race \
                            tickets from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
