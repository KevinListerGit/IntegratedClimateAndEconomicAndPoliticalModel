from django import forms
from django.forms import ModelForm
from .models import ToDoList
from .models import Item

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # check = forms.BooleanField(required = False)

class ItemForm (ModelForm):
    class Meta:
        model = Item
        fields = ['text', 'complete','ToDoList','InstructionDetail']