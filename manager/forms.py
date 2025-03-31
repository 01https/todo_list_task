from django import forms
from django.forms import DateInput

from .models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=DateInput(attrs={"type": "date", "placeholder": "DD/MM/YYYY"})
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]