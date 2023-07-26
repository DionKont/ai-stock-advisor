from django import forms
from django.core.validators import RegexValidator


class StockForm(forms.Form):
    TIME_INTERVAL_CHOICES = [('1', '1min'), ('5', '5min'), ('15', '15min'), ('30', '30min'), ('60', '60min')]
    alpha_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

    stock_name = forms.CharField(max_length=10, validators=[alpha_validator])

    time_interval = forms.ChoiceField(choices=TIME_INTERVAL_CHOICES)
    n_predictions = forms.IntegerField(min_value=0, max_value=5000)
