from django.db import models
from django_pandas.managers import DataFrameManager
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Employee(models.Model):

    full_name = models.CharField(max_length=25)
    age = models.IntegerField()
    department = models.CharField(max_length=3)
    wage = models.FloatField()

    objects = DataFrameManager()

    def __str__(self):
        return self.full_name