from django.db import models

# Create your models here.
# api/models.py
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    age = models.IntegerField()
    objects = models.Manager

    class Meta:
        db_table = "Drf_Test_Table"
