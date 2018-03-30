from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField(max_length=20)
    def __str__(self):
        return self.size

class Colour(models.Model):
    name = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    definition = models.CharField(max_length = 2000)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    image = models.CharField(max_length = 1000)
    def __str__(self):
        return self.name + " - "+str(self.price)

class Bucket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Order(models.Model):
    Bucket = models.ForeignKey(Bucket,on_delete=models.CASCADE)
    completed = models.BooleanField()
    paid = models.BooleanField()
    value = models.FloatField()


class Detail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)

