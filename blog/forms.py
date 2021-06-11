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

