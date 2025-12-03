#created this folder so that we can get the details as per model data
#basically we are going to take the model data same as serializers

from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'