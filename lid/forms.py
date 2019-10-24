import string

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    usern = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class':'input100', 'placeholder':'Enter username'}),
                            label='Login', required=True)
    passw = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':'input100', 'type':'password',
                                'name':'pass', 'placeholder':'Enter Password'}), label='Password', required=True)


class RegisterForm(forms.Form):
    f_name = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class':'input100', 'placeholder':'Enter first name'}),
                            label='First Name', required=True)
    l_name = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class':'input100', 'placeholder':'Enter last name'}),
                            label='Last Name', required=True)
    eml = forms.EmailField(max_length=20,
                            widget=forms.EmailInput(attrs={'class':'input100', 'placeholder':'Enter email'}),
                            label='Email', required=True)
    usern = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class':'input100', 'placeholder':'Enter username'}),
                            label='Login', required=True)
    passw = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':'input100', 'type':'password',
                                'name':'pass', 'placeholder':'Enter Password'}), label='Password', required=True)
    cpassw = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':'input100', 'type':'password',
                                'name':'pass', 'placeholder':'ReEnter Password'}), label='Congim password', required=True)

    def clean(self):
        if self.cleaned_data.get('passw') != self.cleaned_data.get('cpassw'):
            raise forms.ValidationError('Пароли должны совпадать!')
        return self.cleaned_data




class SendMailForm(forms.Form):
    sansw = forms.BooleanField(label='', required=False)