from django.shortcuts import render, get_object_or_404
from .models import Ticket

# Create your views here.

def all_tickets(request):
    """ A view to show all tickets, including sorting and search queries """

    tickets = Ticket.objects.all()

    context = {
        'tickets': tickets,
    }

    return render(request, 'tickets.html', context)


def ticket_detail(request, ticket_id):
    """ A view to show individual ticket details """

    ticket = get_object_or_404(Ticket, pk=ticket_id)

    context = {
        'ticket': ticket,
    }

    return render(request, 'ticket_detail.html', context)