from django import forms
from django.contrib.auth.models import User
from django.db.transaction import commit

from users.models import Profile


class SignUpForm(forms.ModelForm):
    username = forms.CharField(label='Username',
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'class': 'username sign_up',
                                   'placeholder': 'Username'
                               }))
    last_name = forms.CharField(label='Last Name',
                                required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'last_name sign_up',
                                    'placeholder': 'Last Name'
                                }))
    first_name = forms.CharField(label='First Name',
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'first_name sign_up',
                                     'first_name': 'First Name'
                                 }))
    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'email sign_up',
                                 'placeholder': 'Email'
                             }))
    password = forms.CharField(label='Password',
                               required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'password sign_up',
                                   'placeholder': 'Password'
                               }))
    confirm_password = forms.CharField(label='Confirm Password',
                                       required=True,
                                       widget=forms.PasswordInput(attrs={
                                           'class': 'confirm password sign_up',
                                           'placeholder': 'Confirm Password'
                                       }))

    class Meta:
        model = Profile
        fields = ('username', 'last_name', 'first_name', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def save(self):
        profile = super().save(commit=False)
        user = User.objects.create(
            username=profile.username,
            first_name=profile.first_name,
            last_name=profile.last_name,
            email=profile.email
        )
        user.set_password(profile.password)
        user.save()

        profile.user = user
        if commit:
            profile.save()
        return profile

class SignInForm(forms.Form):
    username = forms.CharField(label='Username',
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'class': 'username sign_up',
                                   'placeholder': 'Username'
                               }))
    password = forms.CharField(label='Password',
                               required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'password sign_up',
                                   'placeholder': 'Password'
                               }))

    class Meta:
        model = User
        fields = ['username', 'password']