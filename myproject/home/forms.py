from django import forms
from .models import Student


class DateInput(forms.DateInput):
    input_type = 'date'


class AddForm(forms.ModelForm):
    class Meta:
        model = Student
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
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course'
            }),
            'join_date': DateInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'course': 'Course',
            'join_date': 'Join Date',
        }
