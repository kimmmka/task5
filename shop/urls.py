from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import ProductView, CategoryView, CartView, CommentView, Cart_detailView

app_name = "shop"

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('cart/', CartView.as_view()),
    path('cart_detail/', Cart_detailView.as_view()),
    path('comment/', CommentView.as_view()),
    path('products/<int:pk>', ProductView.as_view(), name='product')
]

'''urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
app_name = "shop"

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    #url(r'^', include('shop.urls', namespace='shop')),
]
'''
