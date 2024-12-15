from django import forms
from .models import *

class PlayerForm(forms.ModelForm):
    class Meta:
        fields = '__all__'