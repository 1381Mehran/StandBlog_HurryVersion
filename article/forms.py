from django import forms
from django.core.validators import ValidationError
from article.models import Contact


class ContactUs(forms.Form):

    name = forms.CharField(max_length=20 , label="Name ")
    email = forms.EmailField()
    subject = forms.CharField(max_length=25)
    body = forms.CharField(max_length=500 , label="Massage" , widget=forms.Textarea)

    def clean(self):

        name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')

        # if 'a' in name :
        #     self.add_error('name' , "a cannot be in name")

        if name == subject :
            raise ValidationError("name and subject cannot be same" , code="name_subject_same")


    def clean_name(self):
        name = self.cleaned_data.get("name")

        if 'a' in name :
            raise ValidationError("a cannot be in name" , code="a_in_name")

        return name

class MassageForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = '__all__'
        # fields = ("name" , 'email' , 'subject' , 'Massage')
        # exclude = ("date",)
        widgets = {
            "name" : forms.TextInput(attrs={
                "class" : "form-control",
                'placeholder' : 'example : Sepehr',
            }),
            "email" : forms.TextInput(attrs={
               'class' : "form-control",
               'placeholder' : 'example@example.com'
            }),
            "subject": forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'create Training Course'
            }),
            "Massage": forms.Textarea(attrs={
                'class' : 'form-control',
            })
        }