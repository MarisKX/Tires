from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from invoices.models import (
    InvoiceItem,
    Invoice,
    Suplier,
)


@receiver(post_save, sender=InvoiceItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem update/create
    """
    item = get_object_or_404(Product, code=instance.product.code)
    item.purchase_price = instance.lineitem_total_with_btw
    print(instance.lineitem_total_with_btw)
    print(item.purchase_price)
    item.save()
    changed_product = get_object_or_404(Product, code=instance.product.code)
    print(changed_product.purchase_price)


@receiver(post_delete, sender=InvoiceItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    item = get_object_or_404(Product, code=instance.product.code)
    item.purchase_price = instance.lineitem_total_with_btw
    item.save()