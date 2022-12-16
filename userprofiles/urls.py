from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('order_history/<ticket_number>', views.order_history, name='order_history'),
]
