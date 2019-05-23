from django import forms
from .models import textpaste
from django.forms import Textarea

class data(forms.ModelForm):
    class Meta:
        model = textpaste
        fields = "__all__"
        widgets = {
            'Text' : Textarea(attrs={'cols': 80, 'rows': 10}),
        }
