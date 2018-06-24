from django.db import models
from django.contrib.auth.models import User

class Constructed(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    chest = models.FloatField()
    height = models.FloatField()
    neck = models.FloatField()
    sleeves = models.FloatField()
    shoulder = models.FloatField()
    blueprint = models.FileField(null=True, blank=True)


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

