from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(label=' name',max_length=20)
    password=forms.CharField(label='password',max_length=20,widget=forms.PasswordInput())