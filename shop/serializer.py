from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Product, Cart, Comment

class ProductSerializer(serializers.Serializer):
    category_name = serializers.CharField(source='category.name')
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.created = validated_data.get('created', instance.created)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    class Meta:
        model=Product
        fields="__all__"

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=200)
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance

class CartSerializer(serializers.Serializer):
    product = serializers.CharField(source='product.title')
    user = serializers.CharField(source='user.username')
    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.products = validated_data.get('products', instance.products)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
    class Meta:
        model=Cart
        fields="__all__"

class CommentSerializer(serializers.Serializer):

    product = serializers.CharField(source='product.title')
    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.content = validated_data.get('content', instance.content)
        instance.creation_date = validated_data.get('creation_date', instance.creation_date)
        instance.replies = validated_data.get('replies', instance.replies)
        instance.product = validated_data.get('replies', instance.replies)
        instance.save()
        return instance
    class Meta:
        model=Comment
        fields="__all__"