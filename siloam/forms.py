from django import forms
from .models import Specialcard


class CardForm(forms.ModelForm):
    class Meta:
        model = Specialcard
        fields = '__all__'
    