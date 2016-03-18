from django.contrib import admin

from core.models import Employee, Fund, Issuer, FundVolumeData, Monthly

# Register your models here.

admin.site.register(Employee)
admin.site.register(Fund)
admin.site.register(Issuer)
admin.site.register(FundVolumeData)
admin.site.register(Monthly)