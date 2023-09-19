from django import forms
from tinymce.widgets import TinyMCE
from .models import *
from django.core import validators


def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError('Kendi denetimimiz.. en az 3 karakter olmali..')


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols':40, 'rows': 20}))
     # 2.yöntem
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message="Oppss.. en az 3 karakter olmali")])
    
        # 3.yöntem 
    title = forms.CharField(validators=[min_length_3])


    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]

        # 1. yöntem
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('Ooo en az 3 karakter olmali')
    #     return title.upper()

        # şekillendirmek için ayrı bi yöntem
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})