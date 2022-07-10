# Generated by Django 4.0.6 on 2022-07-09 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_fb_product_mp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default='AAA001', max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.IntegerField(blank=True, default='00', validators=[django.core.validators.MaxValueValidator(26), django.core.validators.MinValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(blank=True, default='00', validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='season',
            field=models.CharField(choices=[('1', 'No-tires'), ('2', 'Summer'), ('3', 'Winter'), ('4', 'All Season')], default='Summer', max_length=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.IntegerField(blank=True, default='000', validators=[django.core.validators.MaxValueValidator(385), django.core.validators.MinValueValidator(105)]),
        ),
    ]
