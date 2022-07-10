
from django.contrib import admin
from .models import Category, Cars, Manufacturer, Product, Images, ExtraCosts

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


class ImagesAdmin(admin.TabularInline):
    model = Images
    list_display = (
        'product'
    )
    readonly_fields = (
    )


class ExtraCostsAdmin(admin.TabularInline):
    model = ExtraCosts
    list_display = (
        'product',
        'description',
        'amount',
    )
    readonly_fields = (
    )


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImagesAdmin, ExtraCostsAdmin, )
    readonly_fields = (
        'code',
        'full_size',
        'full_size_display',
        'bolt_pattern',
        )
    list_display = (
        'category',
        'code',
        'name',
        'tires',
        'season',
        'full_size_display',
        'width',
        'height',
        'diameter',
        'rims',
        'bolt_pattern',
        'offset',
        'centre_bore',
        'fb',
        'mp',
        'full_costs',
        'price',
    )

    ordering = ('diameter', 'rim_diameter', 'width', 'height', 'stud_count', 'bolt_circle', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
