from csv import list_dialects
from django.contrib import admin
from .models import *

admin.site.register(Profile)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id','nume', 'prenume', 'email', 'telefon', 'adresa')

@admin.register(Product_in_Quote)
class Product_in_QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quote')

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('nume', 'profil', 'culoare', 'sticla')
    list_filter = ('nume', 'profil', 'deschidere', 'culoare', 'sticla')
    list_display = ('id', 'nume', 'profil', 'deschidere', 'culoare', 'sticla')
