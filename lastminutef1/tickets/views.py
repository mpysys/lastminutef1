from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Ticket, Category
from .forms import TicketForm

# Create your views here.

def all_tickets(request):
    """ A view to show all tickets, including sorting and search queries """

    tickets = Ticket.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tickets = tickets.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tickets = tickets.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tickets = tickets.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critera!")
                return redirect(reverse('tickets'))

            queries = Q(race__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query)
            tickets = tickets.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tickets': tickets,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'tickets.html', context)


def ticket_detail(request, ticket_id):
    """ A view to show individual ticket details """

    ticket = get_object_or_404(Ticket, pk=ticket_id)

    context = {
        'ticket': ticket,
    }

    return render(request, 'ticket_detail.html', context)


@login_required
def add_ticket(request):
    """ Add a ticket to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owner of the site can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, 'Successfully added ticket!')
            return redirect(reverse('ticket_detail', args=[ticket.id]))
        else:
            messages.error(request, 'Failed to add ticket. Please ensure the form is valid.')
    else:
        form = TicketForm()
        
    template = 'add_ticket.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_ticket(request, ticket_id):
    """ Edit a ticket in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owner of the site can do that.')
        return redirect(reverse('home'))

    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated ticket!')
            return redirect(reverse('ticket_detail', args=[ticket.id]))
        else:
            messages.error(request, 'Failed to update ticket. Please ensure the form is valid.')
    else:
        form = TicketForm(instance=ticket)
        messages.info(request, f'You are editing {ticket.race}')

    template = 'edit_ticket.html'
    context = {
        'form': form,
        'ticket': ticket,
    }

    return render(request, template, context)


@login_required
def delete_ticket(request, ticket_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owner of the site can do that.')
        return redirect(reverse('home'))
   
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    messages.success(request, 'Ticket deleted!')
    return redirect(reverse('tickets'))
