from django import forms
from .models import textpaste

class data(forms.ModelForm):
    class Meta:
        model = textpaste
        fields = "__all__"
