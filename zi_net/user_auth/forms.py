from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ZiUser

class ZiUserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=13, required=False)
    gender = forms.BooleanField(required=False,)
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=20, required=False)

    class Meta:
        model = ZiUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'phone_number', 'gender', 'birthday', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        return user