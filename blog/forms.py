from django import forms
from tinymce.widgets import TinyMCE
from .models import *
from django.core import validators
from django.forms import widgets


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols':40, 'rows': 20}))
    title = forms.CharField(validators=[validators.MinLengthValidator(3, message="Oppss.. en az 3 karakter olmali")])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment...'})
