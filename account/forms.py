from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))

        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise ValidationError("Username or Password is wrong", code="invalid_info")


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'input-text',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input-text',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text',
        'placeholder': 'Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text',
        'placeholder': 'Confirm Password',
    }))

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return self.cleaned_data.get('password') and self.cleaned_data.get('confirm_password')
        else:
            raise ValidationError('Passwords are not same')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.get(username=username):
            raise ValidationError('User is already exist')
        else:
            return self.cleaned_data.get('username')


class EditForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('first_name' , 'last_name' , 'email' , 'username')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            })
        }
