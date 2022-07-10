# Generated by Django 4.0.6 on 2022-07-09 19:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_code_extracosts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bolt_circle',
            field=models.IntegerField(default='000', validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(98)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='centre_bore',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.IntegerField(default='00', validators=[django.core.validators.MaxValueValidator(26), django.core.validators.MinValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='dot',
            field=models.IntegerField(default='0000', validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='extra_costs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='full_costs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(default='00', validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='offset',
            field=models.IntegerField(default='00', validators=[django.core.validators.MaxValueValidator(65), django.core.validators.MinValueValidator(-15)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='profiel_1',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='profiel_2',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='profiel_3',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='profiel_4',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_document',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rim_diameter',
            field=models.IntegerField(default='00', validators=[django.core.validators.MaxValueValidator(26), django.core.validators.MinValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stud_count',
            field=models.IntegerField(default='0', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.IntegerField(default='000', validators=[django.core.validators.MaxValueValidator(385), django.core.validators.MinValueValidator(105)]),
        ),
    ]