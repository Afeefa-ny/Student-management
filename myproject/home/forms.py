from django import forms
from .models import Employee

class AddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'role': forms.TextInput(attrs={  
                'class': 'form-control',
                'placeholder': 'Enter role'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department'
            }),
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'role': 'Role',              
            'department': 'Department',   
        }