from django import forms


class PredictionForm(forms.Form):

    MALE = 0
    FEMALE = 1

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
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]

    EMBARK_CHOICES = [
        ("", "Select Embark Location"),
        ("Embarked_C", "Cherbourg"),
        ("Embarked_Q", "Queenstown"),
        ("Embarked_S", "Southampton"),
    ]

    ALLOWED_TITLES_BY_GENDER = {
        MALE: {"Mr", "Master", "Rare"},
        FEMALE: {"Miss", "Mrs", "Rare"},
    }

    title = forms.TypedChoiceField(
        choices=TITLE_CHOICES,
        coerce=str,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"}),
    )

    passenger_class = forms.TypedChoiceField(
        choices=PASSENGER_CLASS_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"}),
    )

    gender = forms.TypedChoiceField(
        choices=GENDER_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-control placeholder-select"}),
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

        if gender is None or not title:
            return cleaned_data

        allowed_titles = self.ALLOWED_TITLES_BY_GENDER.get(gender, set())
        if title not in allowed_titles:
            self.add_error("title", "Selected title is not valid for the selected sex.")
            self.add_error("gender", "Selected sex is not valid for the selected title.")

        return cleaned_data
