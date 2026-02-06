from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prediction_form', views.prediction_form, name='prediction_form'),
]
