from django import forms
from .models import Todo

class Todoinfo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todoItem', 'dateToComplete']