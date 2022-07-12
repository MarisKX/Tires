# Generated by Django 4.0.6 on 2022-07-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_suplier_registration_number_or_btw_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default='AA00001', max_length=25),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_paid_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]