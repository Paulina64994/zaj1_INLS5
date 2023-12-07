# forms.py

from django import forms
from .models import TwojModel

class TwojFormularz(forms.ModelForm):
    class Meta:
        model = TwojModel
        fields = ['pole1', 'pole2', ...]  # Lista pól do uwzględnienia w formularzu
