# Generated by Django 4.0.6 on 2022-07-09 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_code_alter_product_diameter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.IntegerField(blank=True, default='00', null=True, validators=[django.core.validators.MaxValueValidator(26), django.core.validators.MinValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(blank=True, default='00', null=True, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.IntegerField(blank=True, default='000', null=True, validators=[django.core.validators.MaxValueValidator(385), django.core.validators.MinValueValidator(105)]),
        ),
    ]
