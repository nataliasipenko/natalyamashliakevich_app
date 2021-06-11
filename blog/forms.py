from .models import Comment
from .models import ClientPost
from django import forms


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

