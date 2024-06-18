from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Category, Product, Rate, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    # prepopulated_fields = {'slug': ('title', )}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_obj', 'price')
    list_display_links = ('id', 'name', 'description_obj', 'price')
    search_fields = ('name', 'id')
    ordering = ('id',)
    def description_obj(self, obj):
        return obj.description[:5]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('product', 'rate')
    search_fields = ('product', 'rate')
    raw_id_fields = ('product',)


@admin.register(Cart)
class CartAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title', 'user')
    search_fields = ('title', 'id')
    ordering = ('id',)