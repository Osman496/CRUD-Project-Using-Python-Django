# This class defines a form for student registration with specific fields and corresponding widgets
# for styling.
from django import forms
from .models import Stu_Data



class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Stu_Data
        fields = ('name', 'age', 'email', 'password','address')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }