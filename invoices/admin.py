
from django.contrib import admin
from .models import Suplier, Invoice, InvoiceItem, Product

# Register your models here.


class SuplierAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'full_name',
        'registration_number_or_btw_number',
        'country',
        'default_opgeld',
    )

    ordering = ('full_name',)


class InvoiceItemAdmin(admin.TabularInline):
    model = InvoiceItem
    list_display = (
        'product',
        'quantity',
        'price',
        'lineitem_total',
        'opgeld_on_item',
        'btw',
        'btw_on_item',
        'btw_on_opgeld',
        'lineitem_total_with_btw'
    )
    readonly_fields = (
        'opgeld_on_item',
        'lineitem_total',
        'btw_on_opgeld',
        'btw',
        'btw_on_item',
        'lineitem_total_with_btw',
    )


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceItemAdmin, )
    readonly_fields = (
        'items_total',
        'opgeld_total',
        'invoice_total',
        'btw_total',
        'amount_total_with_btw',
        'invoice_paid_confirmed',
        )
    list_display = (
        'invoice_number',
        'suplier',
        'date',
        'invoice_paid',
        'invoice_paid_confirmed',
        'items_total',
        'opgeld_total',
        'invoice_total',
        'btw_total',
        'amount_total_with_btw',
    )

    ordering = ('date', 'invoice_number', 'suplier', )


admin.site.register(Suplier, SuplierAdmin)
admin.site.register(Invoice, InvoiceAdmin)
