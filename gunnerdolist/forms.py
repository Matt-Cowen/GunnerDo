from .models import Task
from django import forms
from django.forms import ModelForm


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Add a new task',
            'style': 'margin-bottom: 20px;'
        }),
        label=""
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tactics...',
            'style': 'height: 50px; width: 40%; font-size: 14px; display: block; margin-left: auto; margin-right: auto; margin-bottom: 20px;'
        }),
        label=""
    )
    class Meta:
        model = Task
        fields = ['name', 'progress', 'importance', 'notes']