from django.db import models


# Create your models here.
class Bodymass(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    bmi = models.IntegerField()
    objects = models.manager
