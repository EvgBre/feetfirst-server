from django.db import models
from .order import Order
from .product import Product

class OrderProduct(models.Model):
  
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  order_id = models.ForeignKey(Order, on_delete=models.CASCADE)