from django import forms
from .models import AnkiCard


from django import forms
from .models import AnkiCard


class CardsSetForm(forms.Form):
    set_name = forms.CharField(max_length=100)
    cards = forms.ModelMultipleChoiceField(queryset=AnkiCard.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'card-select', 'size': '5'}))

