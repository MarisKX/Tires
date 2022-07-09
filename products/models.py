from django.db import models
from datetime import *
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator

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
    code = models.CharField(max_length=6, unique=True, default='AA001')
    name = models.CharField(max_length=100, default='name')
    description = models.CharField(max_length=256, default='description')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    tires = models.BooleanField(default=True)

    season_choices = [
        ('1', 'Summer'),
        ('2', 'Winter'),
        ('3', 'All Season'),
    ]
    season = models.CharField(max_length=11, choices=season_choices, default='Summer')
    width = models.IntegerField(default='000', validators=[MaxLengthValidator(3),MinLengthValidator(3)])
    height = models.IntegerField(default='00', validators=[MaxLengthValidator(2),MinLengthValidator(2)])
    diameter = models.IntegerField(default='00', validators=[MaxLengthValidator(2),MinLengthValidator(2)])
    full_size = models.CharField(max_length=10, default='000/00R00')
    full_size_display = models.CharField(max_length=10, default='000/00 R00')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, on_delete=models.SET_NULL)
    dot = models.IntegerField(default='000', validators=[MaxLengthValidator(4),MinLengthValidator(4)])
    profiel_1 = models.DecimalField(max_digits=2, decimal_places=1, blank=False, null=False, default=0.0)
    profiel_2 = models.DecimalField(max_digits=2, decimal_places=1, blank=False, null=False, default=0.0)
    profiel_3 = models.DecimalField(max_digits=2, decimal_places=1, blank=False, null=False, default=0.0)
    profiel_4 = models.DecimalField(max_digits=2, decimal_places=1, blank=False, null=False, default=0.0)

    rims = models.BooleanField(default=True)

    rim_diameter = models.IntegerField(default='00', validators=[MaxLengthValidator(2),MinLengthValidator(2)])
    rim_width = models.CharField(max_length=4, default='0.0J')

    oe_rims = models.BooleanField(default=False)
    oe_number = models.CharField(max_length=50)
    rim_manufacturer = models.ForeignKey('Cars', null=True, blank=True, on_delete=models.SET_NULL)

    stud_count = models.IntegerField(default='0', validators=[MaxLengthValidator(1),MinLengthValidator(1)])
    bolt_circle = models.IntegerField(default='000', validators=[MaxLengthValidator(3),MinLengthValidator(2)])
    bolt_pattern = models.CharField(max_length=5)
    offset = models.IntegerField(default='00', validators=[MaxLengthValidator(3),MinLengthValidator(2)])
    centre_bore = models.DecimalField(max_digits=2, decimal_places=1, blank=False, null=False, default=0.0)

    purchase_price = models.DecimalField(max_digits=4, decimal_places=4, blank=False, null=False, default=0.00)
    extra_costs = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False, default=0.00)
    full_costs = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False, default=0.00)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    archived = models.BooleanField(default=False)
    sold_date = models.DateField(auto_now_add=False)
    sold_price = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False, default=0.00)

    purchase_document = models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the subcategory name
        """
        if self.code == 'AAA001':
            products_count = Product.objects.filter(category=self.category).count()
            self.code = self.category.code + str(products_count + 1).zfill(3)
        super().save(*args, **kwargs)


class Images(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
