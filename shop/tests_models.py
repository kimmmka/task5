from django.test import TestCase
from shop.models import Category,Cart, Cart_detail, Product,Comment

class CommentModelTest(TestCase):
    @classmethod
    def setUpTest(cls):
        comment= Comment.object.create(
            author='user1', rate=1, 
            content="good juice")
        category = Category.objects.create(name='drinks', slug='drinks')
        product = Product.objects.create(title='juice', slug='juice',
                description='bla-bla', product_category="drinks", product_category_slug="drinks", image='ffrf.jpg',
                price = 90,discount=20, suplier='russia')

    def test_Product(cls):
        product_title = Comment.objects.get(id=1).product.title
        product_slug = Comment.objects.get(id=1).product.slug
        product_description = Comment.objects.get(id=1).product.description
        product_image = Comment.objects.get(id=1).product.image
        product_suplier = Comment.objects.get(id=1).product.suplier
        product_discount = Comment.objects.get(id=1).product.discount
        product_price = Comment.objects.get(id=1).product.price
        self.assertEquals(product_title,'juice')
        self.assertEquals(product_slug,'juice')
        self.assertEquals(product_description,'bla-bla')
        self.assertEquals(product_image,'ffrf.jpg')
        self.assertEquals(product_price, 90)
        self.assertEquals(product_discount,20)
        self.assertEquals(product_suplier,'russia')

    def test_Category(self):
        product_category= Product.objects.get(id=1).name
        product_category_slug = Product.objects.get(id=1).slug
        self.assertEquals(product_category,"drinks")
        self.assertEquals(product_category_slug,"drinks")
