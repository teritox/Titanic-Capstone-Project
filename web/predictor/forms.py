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
    
    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder':'0-100'}))
    
    siblings_or_spouses = forms.IntegerField()
    parch = forms.IntegerField()
    ticket_fare = forms.DecimalField(
        min_value=0,
        max_value=500,
        decimal_places=3,  # digits after the decimal
        widget=forms.NumberInput(attrs={'placeholder': 'Enter ticket fare'}))
    
    embark_c = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 if applies'}))
    embark_q = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 if applies'}))
    embark_s = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 if applies'}))