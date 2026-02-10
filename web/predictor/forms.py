from django import forms

class PredictionForm(forms.Form):

    # Choice options with placeholder first
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
        ("Unknown", "Unknown")
    ]

    # TypedChoiceFields to ensure proper types
    passenger_class = forms.TypedChoiceField(
        choices=PASSENGER_CLASS_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"})
    )

    gender = forms.TypedChoiceField(
        choices=GENDER_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"})
    )

    embark = forms.TypedChoiceField(
        choices=EMBARK_CHOICES,
        coerce=str,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"})
    )

    # Integer fields with validation and styling
    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter age"})
    )

    siblings_or_spouses = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of siblings/spouses"})
    )

    parch = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of parents/children"})
    )

    # Ticket fare as DecimalField for precise ML input
    ticket_fare = forms.DecimalField(
        min_value=0,
        max_value=500,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter ticket fare"})
    )
