from django.db import models
from .user import User

class Order(models.Model):
  
  customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
  date_placed = models.DateField()
  payment_type = models.CharField(max_length=30)
  total = models.DecimalField(max_digits=7, decimal_places=2)
  is_completed = models.BooleanField()
