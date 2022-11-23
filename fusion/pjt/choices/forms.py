from django import forms 
from .models import Choice

class ChoiceForm(forms.ModelForm):
    OPTION_A = '5'
    OPTION_B = '10'
    OPTION_C = '15'
    OPTIONS_CHOICES = [
        (OPTION_A, '5개'),
        (OPTION_B, '10개'),
        (OPTION_C, '15개'),
    ]

    option = forms.ChoiceField(
        label="Option",
        choices = OPTIONS_CHOICES,
    )

    class Meta:
        model = Choice
        fields = ('option',)