from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    mob_num = forms.IntegerField(
        label='Mobile Number',
        validators=[
            MaxValueValidator(9999999999, message='Mobile number must be at most 10 digits.'),
            MinValueValidator(0, message='Enter a valid mobile number with only numeric characters.'),
        ],)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'mob_num', 'password1', 'password2']
