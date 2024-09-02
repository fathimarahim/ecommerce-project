from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug','price', 'stock', 'available', 'created', 'updated']

    list_editable = ['price', 'stock', 'available']
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
