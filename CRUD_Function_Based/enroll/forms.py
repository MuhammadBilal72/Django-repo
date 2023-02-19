from django.core import validators
from django import forms
from .models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model=User
        fields=["name","email","password"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}),
            "email":forms.EmailInput(attrs={"class":"form-control","autocomplete":"off"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})

        }