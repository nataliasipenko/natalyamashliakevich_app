from . import models
from .models import Comment
from .models import ClientPost
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ClientPostForm(forms.ModelForm):
    class Meta:
        model = ClientPost
        fields = ('title', 'content', 'file', 'author')


class LoginForm(forms.Form):
    login = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='once again', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords aren't equal")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('birthday', 'photo')
