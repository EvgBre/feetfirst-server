from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=5000)