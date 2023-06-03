from django import forms
from .models import *


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        widgets = {
            'estimated_arrival_time': forms.DateTimeInput(attrs={'class': 'datetimepicker'}, format='%d/%m/%Y %I:%M:%S')
        }


class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'


class UpdateTime(forms.Form):
    estimated_arrival_time = forms.DateTimeField(label="New Date")


class UpdateAddress(forms.Form):
    address = forms.CharField(label="New Address", max_length=200)