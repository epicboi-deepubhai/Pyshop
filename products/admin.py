from django.contrib import admin
from .models import Product, Offer
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = 'Admin Dashboard'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
