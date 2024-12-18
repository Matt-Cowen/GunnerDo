from .models import Task
from django import forms
from django.forms import ModelForm


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task'}), label="")
    notes = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tactics...',
            'style': 'height: 50px; width: 40%; font-size: 14px; display: flex; justify-content: center; align-items: center;'
        })
    )
    class Meta:
        model = Task
        fields = ['name', 'progress', 'importance', 'notes']