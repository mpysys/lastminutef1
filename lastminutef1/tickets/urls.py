from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tickets, name='tickets'),
    path('<ticket_id>', views.ticket_detail, name='ticket_detail'),
]
