from django.db import models

class Store(models.Model):
    owner = models.CharField(max_length=100)

    name = models.CharField(max_length=100)