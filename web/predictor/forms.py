from django import forms

class PredictionForm(forms.Form):
    passenger_class = forms.IntegerField()
    gender = forms.IntegerField()
    age = forms.IntegerField()
    siblings_or_spouses = forms.IntegerField()
    parch = forms.IntegerField()
    ticket_fare = forms.IntegerField()
    embark_c = forms.IntegerField()
    embark_q = forms.IntegerField()
    embark_s = forms.IntegerField()