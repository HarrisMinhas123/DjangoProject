from typing import cast
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)

class category(models.Model):
    name = models.CharField(max_length=255)

class products(models.Model):
    product_name = models.CharField(max_length=255)
    tags = models.ManyToManyField(category, related_name="products")
    category_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    django_admin_side = models.CharField(max_length=255, blank=True)
    