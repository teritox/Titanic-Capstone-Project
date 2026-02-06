from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('history', views.history, name='history'),
    path('result', views.result, name='result'),
    path('prediction_form', views.prediction_form, name='prediction_form'),
]
