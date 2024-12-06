from django import forms
from easybookapp.models import OneWayBooking,BusHiring,ImageModel

class OneWayBookingForm(forms.ModelForm):
    class Meta:
        model = OneWayBooking
        fields = '__all__'


class BusHiringForm(forms.ModelForm):
    class Meta:
        model = BusHiring
        fields = '__all__'


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'