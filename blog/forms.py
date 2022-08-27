from django import forms

from blog.models import *


class AddNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
