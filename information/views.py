from django.shortcuts import render

# Create your views here.


def schedule(request):
    """ A view to return the index page """

    return render(request, 'schedule.html')


def paddock(request):
    """ A view to return the index page """

    return render(request, 'paddock.html')
