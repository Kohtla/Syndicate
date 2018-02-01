from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    definition = models.CharField(max_length = 2000)
    image = models.CharField(max_length = 1000)


    def __str__(self):
        return self.name + " - "+str(self.price)

