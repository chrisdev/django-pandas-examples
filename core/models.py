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


@python_2_unicode_compatible
class Issuer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=5)
    active = models.BooleanField()
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    is_local_entity = models.BooleanField()

    objects = DataFrameManager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Fund(models.Model):
    issuer = models.ForeignKey(Issuer)
    symbol = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    registration_date = models.DateField()
    active = models.BooleanField()
    open_ended = models.BooleanField()
    notes = models.TextField(null=True, blank=True)

    objects = DataFrameManager()

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class Monthly(models.Model):
    dateix = models.DateField(unique=True)

    objects = DataFrameManager()

    def __str__(self):
        return self.dateix.strftime('%Y-%b')

    class Meta:
        verbose_name_plural = 'Monthly'


@python_2_unicode_compatible
class FundVolumeData(models.Model):
    """
    Holds the fund volume data objects
    """
    fund = models.ForeignKey(Fund, limit_choices_to={'active': 'True'})
    period_ending = models.ForeignKey(Monthly, verbose_name="Period",
                        limit_choices_to={'dateix__gte': '2006-12-31'}, blank=False)
    total_unit_holders = models.FloatField(
                        verbose_name="No. Unit holders", blank=True, null=True)
    total_net_assets_under_management = models.FloatField(
                                                null=True, blank=True)

    objects = DataFrameManager()

    def __str__(self):
        return "%s-%s" % (self.fund, self.period_ending)
