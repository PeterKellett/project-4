from django.contrib import admin
from .models import Reviews


# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'user_profile',
        'product_id',
        'comment',
    )


admin.site.register(Reviews, ReviewsAdmin)
