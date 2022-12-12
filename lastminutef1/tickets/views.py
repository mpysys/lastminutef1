from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Ticket, Category

# Create your views here.

def all_tickets(request):
    """ A view to show all tickets, including sorting and search queries """

    tickets = Ticket.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tickets = tickets.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critera!")
                return redirect(reverse('tickets'))

            queries = Q(race__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query)
            tickets = tickets.filter(queries)

    context = {
        'tickets': tickets,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'tickets.html', context)


def ticket_detail(request, ticket_id):
    """ A view to show individual ticket details """

    ticket = get_object_or_404(Ticket, pk=ticket_id)

    context = {
        'ticket': ticket,
    }

    return render(request, 'ticket_detail.html', context)