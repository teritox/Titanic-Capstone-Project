from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'predictor/home.html')


def history(request):
    predictions = []
    return render(request, 'predictor/history.html', {'predictions': predictions})