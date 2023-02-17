from django.core import validators
from django import forms
def start_with_s(value):
    if value[0]!="s":
        raise forms.ValidationError("Name Should Start With S")

class LoginForm(forms.Form):
    name=forms.CharField(error_messages={'required':"Please Enter Your Name"})
    email=forms.CharField(error_messages={'required':"Please Enter Your Email"})

    # password=forms.CharField(widget=forms.PasswordInput())
    # email=forms.EmailField(label="Email Adress",label_suffix=" ",required=False)
    # key=forms.CharField(widget=forms.HiddenInput())
    def clean(self):
        cleaned_data=super().clean()
        valpwd=self.cleaned_data.get("password")
        cpassw=self.cleaned_data.get("rpassword")
        if(valpwd!=cpassw):
            raise forms.ValidationError("Password did not matched")


