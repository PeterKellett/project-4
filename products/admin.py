from django.contrib import admin
from .models import Category, Product, Reviews


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'image_url',
        'image',
        'sku',
        'rating',
        'size_s',
        'size_m',
        'size_lg',
        'size_xl',
    )

    ordering = ('-category',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'user_profile',
        'product_id',
        'comment',
    )


admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
