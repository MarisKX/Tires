# Generated by Django 4.0.6 on 2022-07-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suplier',
            name='registration_number_or_btw_number',
            field=models.CharField(default='NL01', max_length=18, primary_key=True, serialize=False),
        ),
    ]