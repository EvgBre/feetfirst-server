from django.db import models
from .category import Category

class Product(models.Model):

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.CharField(max_length=5000)
    added_on = models.DateField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def favorite(self):
        """custom property to add favorite to a product"""
        return self.__favorite

    @favorite.setter
    def favorite(self, value):
        self.__favorite = value
