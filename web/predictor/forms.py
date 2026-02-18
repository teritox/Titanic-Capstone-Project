from django import forms


class PredictionForm(forms.Form):

    TITLE_CHOICES = [
        ("", "Select Title"),
        ("Master", "Master"),
        ("Miss", "Miss"),
        ("Mrs", "Mrs"),
        ("Mr", "Mr"),
        ("Rare", "Other"),
    ]

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
        ("Embarked_C", "Cherbourg"),
        ("Embarked_Q", "Queenstown"),
        ("Embarked_S", "Southampton"),
    ]

    title = forms.TypedChoiceField(
    choices=TITLE_CHOICES,
    coerce=str,
    widget=forms.Select(attrs={
        "class": "form-control placeholder-select",
        "id": "id_title"
    }),
    )

    passenger_class = forms.TypedChoiceField(
        choices=PASSENGER_CLASS_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"}),
    )

    gender = forms.TypedChoiceField(
    choices=GENDER_CHOICES,
    coerce=int,
    widget=forms.Select(attrs={
        "class": "form-control placeholder-select",
        "id": "id_gender"
    }),
    )

    embark = forms.TypedChoiceField(
        choices=EMBARK_CHOICES,
        coerce=str,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"}),
    )

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter age"}
        ),
    )

    siblings_or_spouses = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Number of siblings/spouses"}
        ),
    )

    parch = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Number of parents/children"}
        ),
    )

    ticket_fare = forms.FloatField(
        min_value=0,
        max_value=500,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter ticket fare"}
        ),
    )

def clean(self):

    cleaned_data = super().clean()
    gender = cleaned_data.get("gender")
    title = cleaned_data.get("title")

    if gender == 0 and title not in ["Master", "Mr", "Rare"]:
        raise forms.ValidationError("Invalid title for Male")


    if gender == 1 and title not in ["Miss", "Mrs", "Rare"]:
        raise forms.ValidationError("Invalid title for Female")

    return cleaned_data

