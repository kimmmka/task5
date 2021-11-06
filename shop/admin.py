from django.contrib import admin
from .models import Comment, Category, Product


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'rate','content','creation_date', 'replies']
admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','price', 'created', 'image', 'discount', 'supplier', 'category']
    list_filter = ['created']
    list_editable = ['price', 'supplier', 'discount']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Product, ProductAdmin)