from django.contrib import admin
from easybookapp.models import OneWayBooking,BusHiring,Contact,Member,ImageModel
# Register your models here.
admin.site.register(OneWayBooking)
admin.site.register(BusHiring)
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(ImageModel)
