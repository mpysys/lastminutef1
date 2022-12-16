from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule, name='information')
]
