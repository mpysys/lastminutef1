from django.shortcuts import render
from .models import Ticket

# Create your views here.

def all_tickets(request):
    """ A view to show all tickets, including sorting and search queries """

    tickets = Ticket.objects.all()

    context = {
        'tickets': tickets,
    }

    return render(request, 'tickets.html', context)