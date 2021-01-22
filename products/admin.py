from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'description',
        'price',
        'image_url',
        'image',
        'sku',
        'size_s',
        'size_m',
        'size_lg',
        'size_xl',
        'number_of_reviews',
    )

    ordering = ('-category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
