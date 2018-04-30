from django import forms

class RegisterForm(forms.Form):
    email = forms.CharField(label='email', max_length=50)
    password = forms.CharField(label='password', max_length=50)
    first_name = forms.CharField(label='first_name', max_length=50)
    last_name = forms.CharField(label='last_name', max_length=50)
    display_name = forms.CharField(label='display_name', max_length=50)