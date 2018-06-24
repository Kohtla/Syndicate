from django.db import models
from django.contrib.auth.models import User

class Constructed(models.Model):
    #user = models.ForeignKey(User,on_delete = models.CASCADE)
    chest = models.FloatField()
    height = models.FloatField()
    neck = models.FloatField()
    sleeves = models.FloatField()
    shoulder = models.FloatField()


class Part(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name


class PartsInPlace(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    constructed = models.ForeignKey(Constructed, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    s = models.FloatField()
    qx = models.FloatField()
    qy = models.FloatField()
    qz = models.FloatField()
    qw = models.FloatField()

