from django.shortcuts import redirect, render
from .models import Prediction
from . import forms
from .forms import PredictionForm
from .ml_model import prediction


def home(request):
    return render(request, "predictor/home.html")


def history(request):
    predictions = Prediction.objects.all().order_by("-timestamp")

    passenger_class_map = dict(PredictionForm.PASSENGER_CLASS_CHOICES[1:])  
    gender_map = dict(PredictionForm.GENDER_CHOICES[1:])
    embark_map = dict(PredictionForm.EMBARK_CHOICES[1:])

    for p in predictions:
        p.passenger_class_label = passenger_class_map.get(p.input_data.get("passenger_class"), "-")
        p.gender_label = gender_map.get(p.input_data.get("gender"), "-")
        p.embark_label = embark_map.get(p.input_data.get("embark"), "-")
        p.probability_percent = round(float(p.prediction_probability) * 100, 2)

    return render(request, "predictor/history.html", {"predictions": predictions})


def result(request):
    prediction_id = request.session.get("prediction_id")

    if not prediction_id:
        return redirect("prediction_form")

    try:
        prediction_obj = Prediction.objects.get(id=prediction_id)
    except Prediction.DoesNotExist:
        return redirect("prediction_form")

    return render(
        request,
        "predictor/result.html",
        {
            "survived": prediction_obj.prediction_result,
            "prediction_probability": prediction_obj.prediction_probability * 100,
        },
    )



def prediction_form(request):
    if request.method == "POST":
        prediction_form = forms.PredictionForm(request.POST)

        if prediction_form.is_valid():
            input_data = prediction_form.cleaned_data

            prediction_result, prediction_probability = prediction(input_data)

            prediction_obj = Prediction.objects.create(
                input_data=input_data,
                prediction_result=prediction_result,
                prediction_probability=prediction_probability,
            )

            request.session["prediction_id"] = prediction_obj.id

            return redirect("result")

    else:
        prediction_form = forms.PredictionForm()

    return render(
        request,
        "predictor/prediction_form.html",
        {"prediction_form": prediction_form},
    )

