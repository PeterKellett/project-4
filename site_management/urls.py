from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_management, name='site_management'),
    path('products/',
         views.site_management_products,
         name='site_management_products'),
    path('orders/',
         views.site_management_orders,
         name='site_management_orders'),
    path('reviews/',
         views.site_management_reviews,
         name='site_management_reviews'),
]
