from django import forms

class PredictionForm(forms.Form):

    PASSENGER_CLASS_CHOICES = [
        ("", "Select Passenger Class"),
        (1, "1st Class"),
        (2, "2nd Class"),
        (3, "3rd Class"),
    ]

    GENDER_CHOICES = [
        ("", "Select Gender"),
        (0, "Male"),
        (1, "Female"),
    ]

    EMBARK_CHOICES = [
        ("", "Select Embark Location"),
        ("C", "Cherbourg"),
        ("Q", "Queenstown"),
        ("S", "Southampton"),
    ]

    passenger_class = forms.ChoiceField(
        choices=PASSENGER_CLASS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"})
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"})
    )

    embark = forms.ChoiceField(
        choices=EMBARK_CHOICES,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"})
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter age"})
    )

    siblings_or_spouses = forms.IntegerField(
        label="Siblings / Spouses Aboard",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of siblings/spouses"})
    )

    parch = forms.IntegerField(
        label="Parents / Children Aboard",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of parents/children"})
    )

    ticket_fare = forms.FloatField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ticket fare"})
    )
