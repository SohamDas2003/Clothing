from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='First Name must contain only alphabets.',
            ),
        ],
    )
    last_name = forms.CharField(
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='Last Name must contain only alphabets.',
            ),
        ],
    )
    mob_num = forms.CharField(
        label='Mobile Number',
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Mobile Number must be a 10-digit numeric value.',
            ),
        ],
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'mob_num', 'password1', 'password2']
