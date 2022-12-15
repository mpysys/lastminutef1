from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tickets, name='tickets'),
    path('<int:ticket_id>', views.ticket_detail, name='ticket_detail'),
    path('add/', views.add_ticket, name='add_ticket'),
]
