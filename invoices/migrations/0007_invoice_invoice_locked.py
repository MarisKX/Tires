# Generated by Django 4.0.6 on 2022-07-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_rename_amount_total_invoice_invoice_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_locked',
            field=models.BooleanField(default=False),
        ),
    ]
