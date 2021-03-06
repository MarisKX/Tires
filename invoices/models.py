from datetime import *
from django.utils import timezone
from django.db import models
from django.db.models import Sum
from products.models import Product
from django.contrib.auth.models import User


class Suplier(models.Model):
    class Meta:
        verbose_name_plural = 'Supliers'

    name = models.CharField(max_length=254, blank=True, null=True)
    full_name = models.CharField(max_length=254, blank=True)
    registration_number_or_btw_number = models.CharField(primary_key=True, max_length=18, default='NL01')
    street_adress_1 = models.IntegerField(default=0, blank=True)
    street_adress_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=100, blank=True)
    default_opgeld = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.full_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the category name
        """
        self.name = self.full_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=25, default='AA00001')
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE, related_name="suplier")
    date = models.DateField(auto_now_add=False)
    invoice_paid = models.BooleanField(default=False)
    invoice_paid_confirmed = models.BooleanField(default=False)
    items_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    opgeld_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    invoice_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    btw_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    amount_total_with_btw = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    invoice_locked = models.BooleanField(default=False)

    def update_invoice_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.items_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.opgeld_total = self.lineitems.aggregate(Sum('opgeld_on_item'))['opgeld_on_item__sum'] or 0
        btw_on_items = self.lineitems.aggregate(Sum('btw_on_item'))['btw_on_item__sum'] or 0
        btw_on_opgeld = self.lineitems.aggregate(Sum('btw_on_opgeld'))['btw_on_opgeld__sum'] or 0
        self.invoice_total = self.items_total + self.opgeld_total
        self.btw_total = btw_on_items + btw_on_opgeld
        self.amount_total_with_btw = self.items_total + self.btw_total + self.opgeld_total
        super().save()

    def __str__(self):
        return self.invoice_number


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, blank=False)
    opgeld_on_item = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, blank=False)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    btw = models.BooleanField(default=True)
    btw_on_item = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0.00)
    btw_on_opgeld = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0.00)
    lineitem_total_with_btw = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.price * self.quantity
        self.opgeld_on_item = self.lineitem_total * (self.invoice.suplier.default_opgeld / 100)
        self.btw_on_opgeld = (self.opgeld_on_item / 100) * 21
        if self.btw:
            self.btw_on_item = (self.lineitem_total / 100) * 21
        self.lineitem_total_with_btw = self.lineitem_total + self.btw_on_item + self.opgeld_on_item + self.btw_on_opgeld
        super().save(*args, **kwargs)