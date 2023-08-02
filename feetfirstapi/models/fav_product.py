from django.db import models
from .product import Product
from .user import User

class FavoriteProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)