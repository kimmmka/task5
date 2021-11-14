from django.test import TestCase,Client
from shop.models import Product, Category, Cart, Comment, Cart_detail
from shop.serializers import ProductSerializer

class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        c=10
        Category.objects.create(name="pizza", slug ="pizza")
        for i in range(i,c+1):
            Product.objects.create(title="margo"+str(i),
             description="delishes"+str(i), price=270, 
             discount=0, supplier="dodo" + str(i),
             category=Category.objects.get(id=1)) 

    def test_all_products(self):
        response=self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

class ProductDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        c=2
        Category.objects.create(name="pizza", slug ="pizza")
        for i in range(i,c+1):
            Product.objects.create(title="margo"+str(i),
             description="delishes"+str(i), price=270, 
             discount=0, supplier="dodo" + str(i),
             category=Category.objects.get(id=1)) 
    
    def test_product_detail_GET(self):
        response = self.client.get(reverse('id', kwargs ={'pk': Product.objects.get(id=1).pk}))
        serializer = ProductSerializer(Product.objects.get(id=1))

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_product_details_GET_invalid(self):
        response = self.client.get(reverse('id', kwargs ={'pk': Product.objects.get(id=1).pk}))
        serializer = ProductSerializer(Product.objects.get(id=2))
        
        self.assertFalse(response.data == serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_product_details_DELETE(self):
        response = self.client.delete(reverse('productsID', kwargs ={'pk': Product.objects.get(id=2).pk}))
        self.assertEquals(response.status_code, 204)