from django import forms
from django.core import validators
from .models import Register_user
'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register_user(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fileds = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(Register_user, self).save(commit=False)
        user.email = self.changed_data['email']
        if commit:
            user.save()
        return user
'''


class Register_user(forms.ModelForm):
    class Meta:
        model = Register_user
        fields = ['first_name', 'last_name', 'email', 'password']
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter your email again')
    password = forms.CharField(widget=forms.PasswordInput)
    verify_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        password = all_clean_data['password']
        verify_password = all_clean_data['verify_password']
        if email != verify_email:
            raise forms.ValidationError('the emails dont mach !\nplease try again')
        if password != verify_password:
            raise forms.ValidationError('the password dont mach !\nplease try again')
