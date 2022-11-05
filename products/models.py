from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=300)
    purchase_price = models.IntegerField()

    def __str__(self):
        return self.name
