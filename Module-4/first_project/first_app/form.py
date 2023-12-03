from typing import Any
from django import forms
from django.core import validators
class contactForm(forms.Form):
    name=forms.CharField(label="User Name", required=False,help_text="Must be a valid user name",  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a user name'}))
    email=forms.EmailField(label="Email")
    age=forms.CharField(widget=forms.NumberInput)
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    birthdate=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    check=forms.BooleanField()
    CHOICE=[('S','Small'),('M','Medium'),('L','Long')]
    size=forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    meal=[('P','Pepperoni'),('M','Mashrooms'),('B','Beef')]
    pizza=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    # file=forms.FileField()

# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.EmailField(widget=forms.EmailInput)
#     def clean(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Please enter a valid name with at least 10 characters")
#     #     return valname
#     # def clean_email(self):
#     #     valemail=self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Please enter .com address")
#     #     return valemail
#         clean_data=super().clean()
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Please enter a valid name with at least 10 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Please enter .com address")
def value_check(value):
    if len(value)<10:
        raise forms.ValidationError("Please enter a valid text with at least 10")
class StudentData(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(35,message='Please enter a valid name with at least 10 characters')])
    text=forms.CharField(validators=[value_check])
    email=forms.EmailField(validators=[validators.EmailValidator()])
    age=forms.IntegerField(validators=[validators.MinValueValidator(24,message="Age at least 25"),validators.MaxValueValidator(35,message="Age at most 30")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(['pdf'],message="File must be .pdf ")])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")
