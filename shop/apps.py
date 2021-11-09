from django.apps import AppConfig


class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment'

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'