
from django.contrib import admin
from .models import Category, Cars, Manufacturer, Product, Images

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
        'category_code',
    )

    ordering = ('display_name',)


class CarsAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )

    ordering = ('display_name',)


class ManufacturerAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )

    ordering = ('display_name',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('code', )
    list_display = (
        'category',
        'code',
        'name',
        'tires',
        'season',
        'full_size_display',
        'rims',
        'bolt_pattern',
        'full_costs',
        'price',
    )

    ordering = ('diameter', 'rim_diameter', 'width', 'height', 'stud_count', 'bolt_circle', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
