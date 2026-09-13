from django import forms


class EnigmaForm(forms.Form):
    senha = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "campo-enigma",
            "placeholder": "...",
            "autocomplete": "off",
            "spellcheck": "false",
        })
    )