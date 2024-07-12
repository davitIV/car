from django import forms
from .models import CarManufacturer, CarBrand, SparePart

class CarManufacturerForm(forms.ModelForm):
    class Meta:
        model = CarManufacturer
        fields = ['name']
        labels = {'name': 'სახელი'}

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']
        labels = {'name': 'სახელი'}

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['name']
        labels = {'name': 'სახელი'}
