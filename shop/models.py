from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Comment(models.Model):
    author = models.CharField(max_length=200, db_index=True)
    rate = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    content = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    replies = models.CharField(max_length=200, db_index=True, default=None)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.content)

         
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(99)])
    supplier = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

 
    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def str(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_sum=models.IntegerField(default=0)
    CHOICES= [(1, 'new'), (2,'paid'),]
    status = models.IntegerField(choices=CHOICES, default=1)
        

class Cart_detail(models.Model):
    cart_id=models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0)
    product = models.ForeignKey('Product', related_name='product', on_delete=models.CASCADE)
    

