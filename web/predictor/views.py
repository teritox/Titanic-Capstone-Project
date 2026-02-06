from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'predictor/home.html')

def prediction_form(request):
    return render(request, 'predictor/prediction_form.html')
