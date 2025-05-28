from django import forms

choices = [
    "traveller",
    "lounger",
    "thriller",
    "artist"
]

class Quiz(forms.Form):
    q1 = forms.ChoiceField(choices=choices)
    q2 = forms.ChoiceField(choices=choices)
    q3 = forms.ChoiceField(choices=choices)