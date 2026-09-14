from django import forms

class EnigmaForm(forms.Form):
    senha = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "campo-enigma",
            "placeholder": "..."
        })
    )