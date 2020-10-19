from django.forms import ModelForm
from .models import *
from django import forms


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = ['employee_name', 'employee_email', 'employee_password', 'employee_age','employee_image']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'employee_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'employee_age': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

        def clean(self):
            pass