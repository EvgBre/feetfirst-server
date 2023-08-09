from django.db import models
from .user import User

class Order(models.Model):
  
  customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
  date_placed = models.DateField(auto_now_add=True)
  open = models.BooleanField(default=True)
