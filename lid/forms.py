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
        super(RegisterForm, self).clean()
        password = self.cleaned_data.get('passw')
        re_password = self.cleaned_data.get('cpassw')
        if not password == re_password:
            self.add_error('passw', 'Пароли не совпадают!')
        has_no = set(password).isdisjoint
        if (len(password) < 8
                or has_no(string.digits)
                or has_no(string.ascii_lowercase)
                or has_no(string.ascii_uppercase)):
                self.add_error('passw', 'Пароль должнен содержать цифры, прописные и строчные буквы(8 символов)!')

        username = self.cleaned_data['usern']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Логин уже зарегестрирован в системе!")
        return username



class SendMailForm(forms.Form):
    sansw = forms.BooleanField(label='', required=False)