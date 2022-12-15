import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from tickets.models import Ticket
from userprofiles.models import UserProfile
# Create your models here.

class TicketOrder(models.Model):
    ticket_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, 
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    discount_value = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_ticket_number(self):
        """
        Generate a random, unique ticket order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for discount_value.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.DISCOUNT_THRESHOLD:
            self.discount_value = 0
        else:
            self.discount_value = self.order_total * settings.STANDARD_DISCOUNT_PERCENTAGE / 100
        self.grand_total = self.order_total - self.discount_value
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the ticket order number
        if it hasn't been set already.
        """
        if not self.ticket_number:
            self.ticket_number = self._generate_ticket_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ticket_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(TicketOrder, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    ticket = models.ForeignKey(Ticket, null=False, blank=False, on_delete=models.CASCADE)
    ticket_days = models.CharField(max_length=2, null=True, blank=True) # Fri; Sat & Sun; Fri, Sat & Sun
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=100, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.ticket.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.ticket.sku} on order {self.order.ticket_number}'