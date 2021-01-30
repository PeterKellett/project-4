from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_management, name='site_management'),
    path('site_management/products',
         views.site_management_products,
         name='site_management_products'),
]
