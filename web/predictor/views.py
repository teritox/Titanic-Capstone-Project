from django.shortcuts import redirect, render
from .models import Prediction
from . import forms
from .ml_model import prediction


def home(request):
    return render(request, "predictor/home.html")


def history(request):
    predictions = []
    return render(request, "predictor/history.html", {"predictions": predictions})


def result(request):
    return render(request, "predictor/result.html")


def prediction_form(request):
    if request.method == "POST":
        prediction_form = forms.PredictionForm(request.POST)

        if prediction_form.is_valid():
            input_data = prediction_form.cleaned_data

            # TODO: Replace with actual model output
            #prediction_result = False
            #prediction_probability = 0.0000

            prediction_result = prediction(input_data)[0]
            prediction_probability = prediction(input_data)[1]

            Prediction.objects.create(
                input_data=input_data,
                prediction_result=prediction_result,
                prediction_probability=prediction_probability,
            )

            return redirect("result")

    else:
        prediction_form = forms.PredictionForm()

    return render(
        request, "predictor/prediction_form.html", {"prediction_form": prediction_form}
    )
