from django.db import models
from datetime import *
from django.utils import timezone
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
    )

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, default="name")
    display_name = models.CharField(max_length=254, null=True, blank=True)
    category_code = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the category name
        """
        if self.name == "name":
            self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class Cars(models.Model):

    class Meta:
        verbose_name_plural = 'Cars'

    name = models.CharField(max_length=254, default="name")
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the category name
        """
        if self.name == "name":
            self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class Manufacturer(models.Model):

    class Meta:
        verbose_name_plural = 'Manufacturers'

    name = models.CharField(max_length=254, default="name")
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the category name
        """
        if self.name == "name":
            self.name = self.display_name.replace(" ", "_").lower()
            super().save(*args, **kwargs)


class Product(models.Model):
    class Meta:
        ordering = ['name']
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=6, unique=True, default='AA0001')
    name = models.CharField(max_length=100, default='name')
    description = models.CharField(max_length=256, default='description')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    tires = models.BooleanField(default=True)

    season_choices = [
        ('1', '-'),
        ('2', 'Summer'),
        ('3', 'Winter'),
        ('4', 'All Season'),
    ]
    season = models.CharField(max_length=11, choices=season_choices, default='Summer')
    width = models.IntegerField(default='000', validators=[MaxValueValidator(385),MinValueValidator(105)], blank=True, null=True)
    height = models.IntegerField(default='00', validators=[MaxValueValidator(80),MinValueValidator(30)], blank=True, null=True)
    diameter = models.IntegerField(default='00', validators=[MaxValueValidator(26),MinValueValidator(12)], blank=True, null=True)
    full_size = models.CharField(max_length=10, default='000/00R00')
    full_size_display = models.CharField(max_length=10, default='000/00 R00')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, on_delete=models.SET_NULL)
    dot = models.IntegerField(default='0000', validators=[MaxValueValidator(9999),MinValueValidator(0000)])
    profiel_1 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, default=0.0)
    profiel_2 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, default=0.0)
    profiel_3 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, default=0.0)
    profiel_4 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, default=0.0)

    rims = models.BooleanField(default=True)

    rim_diameter = models.IntegerField(default='00', validators=[MaxValueValidator(26),MinValueValidator(12)], blank=True, null=True)
    rim_width = models.CharField(max_length=4, default='0.0J', blank=True, null=True)

    oe_rims = models.BooleanField(default=False)
    oe_number = models.CharField(max_length=50, blank=True, null=True)
    rim_manufacturer = models.ForeignKey('Cars', null=True, blank=True, on_delete=models.SET_NULL)

    stud_count = models.IntegerField(default='0', validators=[MaxValueValidator(6),MinValueValidator(3)], blank=True, null=True)
    bolt_circle = models.CharField(max_length=5, default='0', blank=True, null=True)
    bolt_pattern = models.CharField(max_length=5)
    offset = models.IntegerField(default='00', validators=[MaxValueValidator(65),MinValueValidator(-15)], blank=True, null=True)
    centre_bore = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0)

    purchase_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0.00)
    extra_costs = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0.00)
    full_costs = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0.00)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    archived = models.BooleanField(default=False)
    sold_date = models.DateField(auto_now_add=False, blank=True, null=True)
    sold_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0.00)

    purchase_document = models.CharField(max_length=100, blank=True, null=True)
    purchase_date = models.DateField(auto_now_add=False, blank=True, null=True)

    fb = models.BooleanField(default=False)
    mp = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the subcategory name
        """
        if self.code == 'AA0001':
            products_count = Product.objects.filter(category=self.category).count()
            self.code = self.category.category_code + str(products_count + 1).zfill(4)
        if self.width:
            self.full_size = str(self.width) + '/' + str(self.height) + 'R' + str(self.diameter)
            self.full_size_display = str(self.width) + '/' + str(self.height) + ' R' + str(self.diameter)
        else:
            self.full_size = '-'
            self.full_size_display = '-'
        if self.rims:
            self.bolt_pattern = str(self.stud_count) + 'x' + self.bolt_circle
        else:
            self.bolt_pattern = '-'
            self.bolt_circle = '-'
        self.full_costs = self.purchase_price + self.extra_costs
        super().save(*args, **kwargs)



class Images(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class ExtraCosts(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL, related_query_name='extra_costs_product')
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0.00)