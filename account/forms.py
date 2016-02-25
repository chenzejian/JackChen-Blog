from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, help_text='100 characters max.')
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)
    email = forms.EmailField()