from django import forms

class PredictionForm(forms.Form):
    passenger_class = forms.TypedChoiceField(choices=[
        (1, '1st Class'),
        (2, '2nd Class'),
        (3, '3rd Class'),
    ],
    coerce=int,  # converts string → integer
    widget=forms.Select)
    #passenger_class = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1,2 or 3'}))
    #gender = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'O for Male, 1 for Female'}))
    gender = forms.TypedChoiceField(
        choices=[(0, 'Male'),(1, 'Female'),],
        coerce=int,  # converts string → integer
        widget=forms.Select)
    
    age = forms.IntegerField()
    siblings_or_spouses = forms.IntegerField()
    parch = forms.IntegerField()
    ticket_fare = forms.IntegerField()
    embark_c = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 if applies'}))
    embark_q = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 if applies'}))
    embark_s = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 if applies'}))