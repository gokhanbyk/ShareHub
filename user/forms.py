from django import forms
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from .models import *
from django.forms import widgets


class ProfileModelForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'instagram',
            'info',
        ]


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email = email).exists():
            self.add_error('email', 'Bu email mevcut değil!')

        return email

class ChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})