from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ # '__all__' se quiser utilizar todos os campos do forms do django # noqa
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
