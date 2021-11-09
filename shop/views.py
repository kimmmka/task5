from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
#from .cart import Cart
from .models import Product,Category, Cart, Comment
#from cart.forms import CartAddProductForm
from .serializer import ProductSerializer, CategorySerializer, CartSerializer, CommentSerializer

class ProductView(APIView):
    def get(self, request):
        products=Product.objects.all()
        return Response({"products":products})
    def post(self, request):
        product = request.data.get('product')
        # Create an article from the above data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.title)})
    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('product')
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({
            "success": "Product '{}' updated successfully".format(product_saved.title)
        })
    def delete(self, request, pk):
        # Get object with this pk
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({
            "message": "Product with id `{}` has been deleted.".format(pk)
        }, status=204)
        
class CategoryView(APIView):
    def get(self, request):
        categories=Category.objects.all()
        return Response({"categories": categories})
    def post(self, request):
        category = request.data.get('category')
        # Create an article from the above data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.title)})
    def put(self, request, pk):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data.get('category')
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({
            "success": "Category '{}' updated successfully".format(category_saved.title)
        })
    def delete(self, request, pk):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()
        return Response({
            "message": "Category with id `{}` has been deleted.".format(pk)
        }, status=204)

class CartView(APIView):
    def get(self, request):
        carts=Cart.objects.all()
        return Response({"carts": carts})

    def post(self, request):
        cart = request.data.get('cart')
        # Create an article from the above data
        serializer = CartSerializer(data=cart)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
        return Response({"success": "Cart '{}' created successfully".format(cart_saved.title)})
    def put(self, request, pk):
        saved_cart = get_object_or_404(Cart.objects.all(), pk=pk)
        data = request.data.get('cart')
        serializer = CartSerializer(instance=saved_cart, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
        return Response({
            "success": "Cart '{}' updated successfully".format(cart_saved.title)
        })
    def delete(self, request, pk):
        # Get object with this pk
        cart = get_object_or_404(Cart.objects.all(), pk=pk)
        cart.delete()
        return Response({
            "message": "Cart with id `{}` has been deleted.".format(pk)
        }, status=204)

class CommentView(APIView):
    def get(self, request):
        comments=Comment.objects.all()
        return Response({"comments": comments})

    def post(self, request):
        comment = request.data.get('comment')
        # Create an article from the above data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({"success": "Comment '{}' created successfully".format(comment_saved.title)})
    def put(self, request, pk):
        saved_comment = get_object_or_404(Comment.objects.all(), pk=pk)
        data = request.data.get('comment')
        serializer = CommentSerializer(instance=saved_comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({
            "success": "Comment '{}' updated successfully".format(comment_saved.title)
        })
    def delete(self, request, pk):
        # Get object with this pk
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()
        return Response({
            "message": "Comment with id `{}` has been deleted.".format(pk)
        }, status=204)

