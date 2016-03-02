from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.

class Employee(models.Model):

    full_name = models.CharField(max_length=25)
    age = models.IntegerField()
    department = models.CharField(max_length=3)
    wage = models.FloatField()

    objects = DataFrameManager()