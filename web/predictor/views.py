from django.shortcuts import render
from . import forms

# Create your views here.

def home(request):
    return render(request, 'predictor/home.html')


def history(request):
    predictions = []
    return render(request, 'predictor/history.html', {'predictions': predictions})


def result(request):
    return render(request, 'predictor/result.html')


def prediction_form(request):
    prediction_form = forms.PredictionForm()

    if request.method == 'POST':
        form = forms.PredictionForm(request.POST)

        #If form is valid
            #Add to database
            #return to result page



    return render(request, 'predictor/prediction_form.html', {'prediction_form': prediction_form})
