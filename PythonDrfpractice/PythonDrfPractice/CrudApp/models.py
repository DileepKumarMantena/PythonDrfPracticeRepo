from django.db import models


# Create your models here.
class RegistrationModel(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    objects=models.Manager

    class Meta:
        db_table = "RegisterTable"
