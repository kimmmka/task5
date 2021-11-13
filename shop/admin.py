from django.contrib import admin
from .models import Category, Product, Cart, Comment


admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Cart)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','price', 'created', 'image', 'discount', 'supplier', 'category']
    list_filter = ['created']
    list_editable = ['price', 'supplier', 'discount']
    prepopulated_fields = {'slug': ('title',)}
#admin.site.register(Product, ProductAdmin)
