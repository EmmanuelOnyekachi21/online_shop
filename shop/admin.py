from django.contrib import admin

# Register your models here.
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'available',
        'created',
        'updated'
    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.

    Attributes:
        list_display (list): Fields to display in the admin list view.
        prepopulated_fields (dict): Fields that are auto-filled based on other fields.
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}