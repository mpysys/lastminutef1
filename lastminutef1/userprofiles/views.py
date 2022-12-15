from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import TicketOrder

# Create your views here.


@login_required
def user_profile(request):
    """ Display the user's profile"""
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=userprofile)
    orders = userprofile.orders.all()
    print(orders)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, ticket_number):
    ticket_order = get_object_or_404(TicketOrder, ticket_number=ticket_number)

    messages.info(request, (
        f'This is a past confirmation for order number {ticket_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout_success.html'
    context = {
        'ticket_order': ticket_order,
        'from_profile': True,
    }

    return render(request, template, context)
